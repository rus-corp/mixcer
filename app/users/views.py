from django.shortcuts import render
from rest_framework import generics, status, permissions
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.authentication import authenticate
from drf_spectacular.utils import extend_schema

from .scheme.scheme import KnoxTokenScheme
from knox.views import LoginView as KnoxLoginView


from .models import CustomUser
from .serializers import RegisterUserSerializer, CustomUserSerializer, LoginUserSerializer



class RegisterUserView(generics.CreateAPIView):
    serializer_class=  RegisterUserSerializer
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, *args, **kwargs):
        if {'email', 'password', 'password_confirm'}.issubset(request.data):
            try:
                validate_password(request.data['password'])
            except ValidationError as error:
                return Response({'Status': False, 'error': error.message}, status=status.HTTP_403_FORBIDDEN)
            
            user_serializer = CustomUserSerializer(data=request.data)
            if user_serializer.is_valid():
                user = user_serializer.save()
                user.set_password(request.data['password'])
                user.save()
                return Response({'Status': True, 'message': 'Вы зарегестрированы'}, status=status.HTTP_200_OK)
            else:
                return Response({'Status': False, 'erors': user_serializer.errors}, status=status.HTTP_403_FORBIDDEN)
        return Response({'Status': False, 'error': 'Не указаны обязательные поля'}, status=status.HTTP_400_BAD_REQUEST)
            
            
            
class LoginView(KnoxLoginView):
    serializer_class = LoginUserSerializer
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None, *args, **kwargs):
        if {'email', 'password'}.issubset(request.data):
            user = authenticate(request, email=request.data['email'], password=request.data['password'])
            if user is not None:
                if user.is_active:
                    request.user = user
                    return super(LoginView, self).post(request, format=None)
                else:
                    return Response({'Status': False, 'error': 'Пользователь не активен'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'Status': False, 'error': 'Пользователь не найден'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'Status': False, 'error': 'Не указаны все обязательные поля'}, status=status.HTTP_400_BAD_REQUEST)
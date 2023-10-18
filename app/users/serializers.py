from rest_framework import serializers

from .models import CustomUser


class RegisterUserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password_confirm']
        
    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs
        
        
class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email', 'password',)
        
        
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email','phone_number']
        read_only_fields = ['id',]
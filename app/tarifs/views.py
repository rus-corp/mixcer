from django.shortcuts import render
from rest_framework import viewsets, permissions


from .models import UserTarif
from app.content.models import Content
from .serializers import ContentTarifSerializer, UserTarifSerializer, ListUserTarifSerializer


class TarifViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentTarifSerializer
    
    
    
class TarifChoiceViewSet(viewsets.ModelViewSet):
    queryset = UserTarif.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserTarifSerializer
        else:
            return ListUserTarifSerializer
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    


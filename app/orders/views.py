from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions


from .models import Order
from .serializaers import OrderSerializer, OrderContentSerializer


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
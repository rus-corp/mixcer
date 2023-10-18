from rest_framework import serializers


from .models import Order, OrderContent
from app.content.serializaers import ContentSerializer
from app.content.models import Content
from app.users.serializers import CustomUserSerializer





class OrderContentSerializer(serializers.ModelSerializer):
    content= ContentSerializer()
    class Meta:
        model = OrderContent
        fields = ['id', 'fyle_type', 'screen_resolution', 'fon', 'scenario', 'table_rotation', 'shot_count', 'content']
        read_only_fields = ['user', 'price']



class OrderSerializer(serializers.ModelSerializer):
    ordercontent = OrderContentSerializer(many=True)
    user = CustomUserSerializer()
    class Meta:
        model = Order
        fields = ['id', 'user', 'ordercontent']
        read_only_fields = ['user',]
        
        
    def create(self, validated_data):
        ordercontent_data = validated_data.pop('ordercontent')
        order = Order.objects.create(user=validated_data['user'])
        for item in ordercontent_data:
            content_data = item.pop('content')
            content = Content.objects.get(**content_data)
            order_content = OrderContent.objects.create(order=order, **item, content=content)
            
            order_content.save()
            
        return order
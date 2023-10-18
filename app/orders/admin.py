from django.contrib import admin

from .models import Order, OrderContent


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']
    
    
@admin.register(OrderContent)
class OrderContent(admin.ModelAdmin):
    list_display = ['id', 'order', 'shot_count', 'content']
    
    
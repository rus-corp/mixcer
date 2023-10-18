from django.contrib import admin

from .models import BasePrice, Content


@admin.register(BasePrice)
class BasePriceAdmin(admin.ModelAdmin):
    list_display = ['value']
    
    
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['name', 'coef', 'price']
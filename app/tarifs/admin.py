from django.contrib import admin

from .models import Tarif, UserTarif

@admin.register(Tarif)
class TarifAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'shot_count', 'discount', 'get_total_price']
    
    
@admin.register(UserTarif)
class UserTarifAdmin(admin.ModelAdmin):
    list_display = ['user', 'tarif', 'shot_remains']
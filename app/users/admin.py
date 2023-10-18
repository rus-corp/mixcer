from django.contrib import admin

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone_number', 'email_confirm']
    save_on_top = True
    list_display_links = ['email',]
    search_fields = ['email', 'phone_number']
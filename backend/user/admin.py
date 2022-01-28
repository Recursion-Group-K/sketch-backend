from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'password', 'is_active')
    list_filter = ('is_active',)
    fieldsets = [
      ('User information', {'fields': ['username', 'email', 'password', 'is_active']}),
    ]

admin.site.register(User, UserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Infos supplémentaires', {'fields': ('role', 'phone', 'avatar')}),
    )


admin.site.register(User, CustomUserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from django.contrib.auth.models import Group

# Register your models here.


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'phoneNumber', 'email_verified_at', 'is_superuser')
    list_filter = ('is_superuser',)
    readonly_fields = ('last_login',)

    fieldsets = (
        ("Main", {'fields': ('username', 'email', 'first_name',
         'last_name', 'phoneNumber', 'image','email_verified_at', 'is_superuser')}),
        ('Permissions',
         {'fields': ('is_active', 'is_staff', 'last_login')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'email',
                           'password')}),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ()


# admin.site.unregister(Group)
admin.site.register(User, UserAdmin)

from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin, Group


class UserAdminConfig(UserAdmin):
    list_filter = ('username', 'email', 'avatar', 'phone', 'gender', 'creation_date', 'update_date')
    list_display = ('id', 'username', 'email', 'avatar', 'phone', 'gender', 'creation_date', 'update_date')
    list_display_links = ('id', 'username', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Info', {'fields': ('avatar', 'phone', 'gender')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')})
    )


admin.site.unregister(Group)
admin.site.register(User, UserAdminConfig)

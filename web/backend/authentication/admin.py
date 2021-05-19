from django.contrib import admin
from  .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.


@admin.register(User)
class UserAdmin(UserAdmin,):
    """
    Model for user Admin
    """

    list_display = ('id', 'username', 'is_active', 'name', 'email', 'contact_no')
    list_filter = ('is_active',)
    search_fields = ('contact_no', 'email', 'name')
    fieldsets = (
        (_('Basic details'), {
            'fields': ('name', 'email', 'contact_no',)
        }),
        ('Authentication', {
            'fields': ('username', 'password')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
        }),
    )

    class Meta:
        model = User

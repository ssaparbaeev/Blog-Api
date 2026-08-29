from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUserModel


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel
    list_display = [
        'email',
        'username',
        'name',
        'is_staff',
    ]

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("name",)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'name', 'password1', 'password2'),
        }),
    )


admin.site.register(CustomUserModel, CustomUserAdmin)

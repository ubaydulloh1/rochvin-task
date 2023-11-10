from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_display = ("pk", "username", "email", "is_active", "is_staff", "is_superuser", "date_joined")
    list_display_links = ("pk", "username", "email")
    list_filter = ("is_staff", "is_active", "is_superuser",)
    search_fields = ("username", "email")
    add_fieldsets = (
        (None, {
            "fields": ("username", "email", "password1", "password2"),
        }),
    )


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "first_name", "last_name", "middle_name", "created_at",)
    list_display_links = ("pk", "user")
    search_fields = ("user__username", "user__email", "first_name", "last_name", "middle_name")
    autocomplete_fields = ("user",)


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "first_name", "last_name", "middle_name", "created_at",)
    list_display_links = ("pk", "user")
    search_fields = ("user__username", "user__email", "first_name", "last_name", "middle_name")
    autocomplete_fields = ("user",)

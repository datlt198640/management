from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .form import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(UserAdmin):
    model = User
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ("username", "first_name", "last_name", "is_staff")
    list_filter = ("phone_number", "email", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": ("phone_number", "email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, UserAdmin)
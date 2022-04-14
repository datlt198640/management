from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Staff


class StaffAdmin(admin.ModelAdmin):
    model = Staff
    list_display = ("full_name", "gender", "dob", "address")


admin.site.register(Staff, StaffAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "username",
        "email",
        "is_superuser",
    ]

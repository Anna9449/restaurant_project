from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import RestaurantUser


@admin.register(RestaurantUser)
class UserAdmin(BaseUserAdmin):
    pass

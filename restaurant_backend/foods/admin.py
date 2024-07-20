from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Food,  FoodCategory


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_ru'
    )
    list_display_links = ('name_ru',)
    search_fields = ('name_ru', 'name_en', 'name_ch')


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_ru',
        'category',
        'is_publish',
        'is_vegan'
    )
    list_display_links = ('name_ru',)
    list_filter = ('is_publish', 'is_vegan', 'category__name_ru')
    search_fields = ('name_ru', 'name_en', 'name_ch')


admin.site.unregister(Group)

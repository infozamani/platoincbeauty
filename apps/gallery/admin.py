from django.contrib import admin
from .models import GalleryItem


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'gender', 'is_active', 'order')
    list_filter = ('category', 'gender', 'is_active')
    list_editable = ('is_active', 'order')
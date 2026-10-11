from django.contrib import admin
from .models import Service, ServiceCategory


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for ServiceCategory model.
    Note: ServiceCategory has no 'is_active' field — only Service does.
    """
    list_display = ('name', 'slug', 'order')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Admin configuration for Service model.
    """
    list_display = ('name', 'gender', 'category', 'price', 'duration_minutes', 'is_active')
    list_filter = ('gender', 'is_active', 'category')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active',)
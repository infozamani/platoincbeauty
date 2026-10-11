from django.contrib import admin
from .models import Stylist


@admin.register(Stylist)
class StylistAdmin(admin.ModelAdmin):
    """
    Admin configuration for Stylist model.
    """
    list_display = ('display_name', 'is_active', 'order', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('display_name', 'bio')
    prepopulated_fields = {'slug': ('display_name',)}
    filter_horizontal = ('specialties',)
    list_editable = ('is_active', 'order')
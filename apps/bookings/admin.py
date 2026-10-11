from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for Booking model.
    Allows staff to confirm, cancel, or complete bookings.
    """
    list_display = ('customer_name', 'service', 'stylist', 'start_datetime', 'status')
    list_filter = ('status', 'stylist', 'service')
    search_fields = ('customer_name', 'customer_phone', 'customer_email')
    date_hierarchy = 'start_datetime'
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
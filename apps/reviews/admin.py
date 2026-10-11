from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'stylist', 'rating', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'rating', 'stylist')
    list_editable = ('is_approved',)
    search_fields = ('customer_name', 'comment')
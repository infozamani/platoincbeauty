from django.contrib import admin
from .models import InitialData


@admin.register(InitialData)
class InitialDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'updated_at')
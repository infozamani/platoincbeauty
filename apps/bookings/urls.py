from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.booking_create, name='create'),
    path('success/', views.booking_success, name='success'),
    path('lookup/', views.booking_lookup, name='lookup'),
    path('api/slots/<int:stylist_id>/', views.api_available_slots, name='api_slots'),
]
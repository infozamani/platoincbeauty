from django.urls import path
from . import views

app_name = 'stylists'

urlpatterns = [
    # List all stylists: /stylists/
    path('', views.stylist_list, name='list'),

    # Stylist detail: /stylists/<slug>/
    path('<slug:slug>/', views.stylist_detail, name='detail'),
]
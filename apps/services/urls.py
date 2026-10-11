from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    # List all services: /services/
    path('', views.service_list, name='list'),

    # Service detail: /services/<slug>/
    path('<slug:slug>/', views.service_detail, name='detail'),
]
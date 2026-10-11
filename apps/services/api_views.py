from rest_framework import viewsets
from .models import Service, ServiceCategory
from .serializers import ServiceSerializer, ServiceCategorySerializer


class ServiceCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for service categories.
    Read-only: list and retrieve.
    """
    queryset = ServiceCategory.objects.all()   # ← این خط اصلاح شد
    serializer_class = ServiceCategorySerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for services.
    Supports filtering by gender and category via query params.
    """
    queryset = Service.objects.filter(is_active=True)   # ← این درست است، چون Service فیلد is_active دارد
    serializer_class = ServiceSerializer
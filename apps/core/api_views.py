from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import InitialData
from .serializers import InitialDataSerializer


class InitialDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InitialData.objects.all()
    serializer_class = InitialDataSerializer
    permission_classes = [AllowAny]
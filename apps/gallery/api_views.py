from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import GalleryItem
from .serializers import GalleryImageSerializer


class GalleryImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['gender', 'stylist', 'service', 'is_featured']
from rest_framework import serializers
from .models import GalleryItem


class GalleryImageSerializer(serializers.ModelSerializer):
    stylist_name = serializers.CharField(source='stylist.display_name', read_only=True)
    service_name = serializers.CharField(source='service.name', read_only=True)

    class Meta:
        model = GalleryItem
        fields = (
            'id', 'title', 'image', 'gender', 'stylist', 'stylist_name',
            'service', 'service_name', 'is_featured', 'order', 'created_at',
        )
        read_only_fields = ('id', 'created_at')
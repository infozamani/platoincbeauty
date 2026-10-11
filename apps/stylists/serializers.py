from rest_framework import serializers
from .models import Stylist
from apps.services.serializers import ServiceSerializer


class StylistSerializer(serializers.ModelSerializer):
    """
    Serializer for Stylist model, used by the REST API.
    Includes nested specialties for mobile clients.
    """
    specialties = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Stylist
        fields = [
            'id', 'display_name', 'slug', 'bio', 'photo',
            'specialties', 'is_active', 'order',
        ]
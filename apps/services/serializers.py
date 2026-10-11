from rest_framework import serializers
from .models import Service, ServiceCategory


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'slug', 'order']


class ServiceSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer(read_only=True)
    gender_display = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'slug', 'description', 'gender', 'gender_display',
            'category', 'duration_minutes', 'price', 'image', 'is_active',
        ]
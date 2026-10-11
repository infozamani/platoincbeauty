from rest_framework import serializers
from .models import InitialData


class InitialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialData
        fields = '__all__'
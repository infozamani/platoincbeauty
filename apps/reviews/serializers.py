from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.username', read_only=True)
    stylist_name = serializers.CharField(source='stylist.display_name', read_only=True)

    class Meta:
        model = Review
        fields = (
            'id', 'booking', 'customer', 'customer_name',
            'stylist', 'stylist_name', 'rating', 'comment',
            'is_approved', 'created_at',
        )
        read_only_fields = ('id', 'customer', 'stylist', 'is_approved', 'created_at')
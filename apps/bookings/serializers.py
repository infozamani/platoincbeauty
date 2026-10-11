from rest_framework import serializers
from .models import Booking
from apps.services.serializers import ServiceSerializer
from apps.stylists.serializers import StylistSerializer


class BookingSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    stylist = StylistSerializer(read_only=True)
    service_id = serializers.IntegerField(write_only=True)
    stylist_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Booking
        fields = (
            'id', 'customer', 'stylist', 'stylist_id', 'service', 'service_id',
            'start_datetime', 'end_datetime', 'status', 'notes',
            'created_at', 'updated_at',
        )
        read_only_fields = ('id', 'customer', 'end_datetime', 'status', 'created_at', 'updated_at')

    def validate(self, attrs):
        from apps.services.models import Service
        from apps.stylists.models import Stylist
        from datetime import timedelta

        try:
            service = Service.objects.get(id=attrs['service_id'])
            stylist = Stylist.objects.get(id=attrs['stylist_id'])
        except (Service.DoesNotExist, Stylist.DoesNotExist):
            raise serializers.ValidationError('Invalid service or stylist.')

        start = attrs['start_datetime']
        end = start + timedelta(minutes=service.duration_minutes)

        # بررسی تداخل زمانی
        conflict = Booking.objects.filter(
            stylist=stylist,
            status__in=['pending', 'confirmed'],
            start_datetime__lt=end,
            end_datetime__gt=start,
        ).exists()

        if conflict:
            raise serializers.ValidationError('This time slot is already booked.')

        attrs['service'] = service
        attrs['stylist'] = stylist
        attrs['end_datetime'] = end
        return attrs

    def create(self, validated_data):
        validated_data.pop('service_id', None)
        validated_data.pop('stylist_id', None)
        validated_data['customer'] = self.context['request'].user
        return super().create(validated_data)
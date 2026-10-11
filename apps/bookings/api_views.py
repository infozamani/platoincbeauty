from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Booking
from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'manager':
            return Booking.objects.all()
        if user.role == 'stylist':
            return Booking.objects.filter(stylist__user=user)
        return Booking.objects.filter(customer=user)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        booking = self.get_object()
        if booking.status in ['cancelled', 'completed']:
            return Response({'detail': 'Booking cannot be cancelled.'}, status=status.HTTP_400_BAD_REQUEST)
        booking.status = 'cancelled'
        booking.save()
        return Response({'detail': 'Booking cancelled.', 'status': booking.status})
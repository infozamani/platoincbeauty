from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Stylist
from .serializers import StylistSerializer


class StylistViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for stylists.
    Read-only: list and retrieve.
    """
    queryset = Stylist.objects.filter(is_active=True)
    serializer_class = StylistSerializer
    lookup_field = 'slug'

    @action(detail=True, methods=['get'])
    def availability(self, request, slug=None):
        """
        Custom action: return available time slots for a stylist on a given date.
        Query param: ?date=YYYY-MM-DD
        """
        from apps.bookings.views import api_available_slots
        stylist = self.get_object()
        return api_available_slots(request, stylist.id)
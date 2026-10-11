from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = Review.objects.filter(is_approved=True)
        stylist_id = self.request.query_params.get('stylist')
        if stylist_id:
            qs = qs.filter(stylist_id=stylist_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
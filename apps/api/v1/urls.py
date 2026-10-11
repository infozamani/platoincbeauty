from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.accounts.api_views import RegisterView, LoginView, ProfileView
from apps.services.api_views import ServiceViewSet, ServiceCategoryViewSet
from apps.stylists.api_views import StylistViewSet
from apps.bookings.api_views import BookingViewSet
from apps.reviews.api_views import ReviewViewSet
from apps.gallery.api_views import GalleryImageViewSet
from apps.blog.api_views import BlogPostViewSet, BlogCategoryViewSet
from apps.core.api_views import InitialDataViewSet


router = DefaultRouter()
router.register('services', ServiceViewSet, basename='service')
router.register('service-categories', ServiceCategoryViewSet, basename='service-category')
router.register('stylists', StylistViewSet, basename='stylist')
router.register('bookings', BookingViewSet, basename='booking')
router.register('reviews', ReviewViewSet, basename='review')
router.register('gallery', GalleryImageViewSet, basename='gallery')
router.register('blog', BlogPostViewSet, basename='blog')
router.register('blog-categories', BlogCategoryViewSet, basename='blog-category')
router.register('salon-info', InitialDataViewSet, basename='salon-info')


urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='api-register'),
    path('auth/login/', LoginView.as_view(), name='api-login'),
    path('auth/profile/', ProfileView.as_view(), name='api-profile'),
    path('', include(router.urls)),
]
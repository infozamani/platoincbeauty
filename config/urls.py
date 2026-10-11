from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/', include('apps.api.v1.urls')),

    path('', include('apps.core.urls')),
    path('services/', include('apps.services.urls')),
    path('stylists/', include('apps.stylists.urls')),
    path('bookings/', include('apps.bookings.urls')),
    path('gallery/', include('apps.gallery.urls')),
    path('blog/', include('apps.blog.urls')),
    path('reviews/', include('apps.reviews.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
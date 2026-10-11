from django.db import models
from django.conf import settings


class Stylist(models.Model):
    """
    A stylist (hairdresser) working at the salon.
    Each stylist may be linked to a User account for login purposes.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='stylist_profile',
        null=True,
        blank=True,
    )
    display_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='stylists/', blank=True, null=True)
    specialties = models.ManyToManyField(
        'services.Service',
        blank=True,
        related_name='stylists',
    )
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'display_name']

    def __str__(self):
        return self.display_name
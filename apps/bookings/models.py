from django.db import models
from django.conf import settings
from apps.services.models import Service
from apps.stylists.models import Stylist


class Booking(models.Model):
    """
    A booking made by a customer for a specific service with a specific stylist.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
        ('no_show', 'No Show'),
    ]

    # Customer info — no account required for booking
    customer_name = models.CharField(max_length=150)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField(blank=True)

    # Optional link to a registered user
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='bookings',
    )

    # Service & stylist
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='bookings')
    stylist = models.ForeignKey(Stylist, on_delete=models.PROTECT, related_name='bookings')

    # Date & time
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    # Status & notes
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_datetime']
        indexes = [
            models.Index(fields=['stylist', 'start_datetime']),
            models.Index(fields=['status', 'start_datetime']),
        ]

    def __str__(self):
        return f"{self.customer_name} - {self.service.name} @ {self.start_datetime:%Y-%m-%d %H:%M}"
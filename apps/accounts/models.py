from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model for PlatonicBeauty."""

    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('stylist', 'Stylist'),
        ('manager', 'Manager'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username
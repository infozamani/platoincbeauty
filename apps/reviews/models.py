from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.stylists.models import Stylist


class Review(models.Model):
    """
    A customer review for a stylist.
    Reviews require admin approval before they appear publicly.
    """
    customer_name = models.CharField(max_length=150)
    stylist = models.ForeignKey(
        Stylist,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.customer_name} → {self.stylist.display_name} ({self.rating}★)"
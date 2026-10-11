from django.db import models


class GalleryItem(models.Model):
    """
    An image in the salon's public gallery.
    Can be tagged by category (hair, nails, makeup, etc.) and gender.
    """
    CATEGORY_CHOICES = [
        ('hair', 'Hair'),
        ('nails', 'Nails'),
        ('makeup', 'Makeup'),
        ('skin', 'Skin'),
        ('other', 'Other'),
    ]
    GENDER_CHOICES = [
        ('male', 'Men'),
        ('female', 'Women'),
        ('unisex', 'Unisex'),
    ]

    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='unisex')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title or f"Gallery item #{self.id}"
from django.db import models


class InitialData(models.Model):
    """Salon basic info (singleton record)."""

    name = models.CharField(max_length=200, default='PlatonicBeauty')
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    about_text = models.TextField(blank=True)
    logo = models.ImageField(upload_to='core/', blank=True, null=True)
    open_hours = models.CharField(max_length=200, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Salon Info'
        verbose_name_plural = 'Salon Info'

    def __str__(self):
        return self.name
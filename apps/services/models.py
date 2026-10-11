from django.db import models


class ServiceCategory(models.Model):
    """
    Category for grouping services (e.g., Haircut, Coloring, Spa).
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Service Categories'

    def __str__(self):
        return self.name


class Service(models.Model):
    """
    A specific service offered by the salon.
    Can be for men, women, or unisex.
    """
    GENDER_CHOICES = [
        ('male', 'Men'),
        ('female', 'Women'),
        ('unisex', 'Unisex'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='unisex')
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='services',
    )
    duration_minutes = models.PositiveIntegerField(default=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_gender_display()})"
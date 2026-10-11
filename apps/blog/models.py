from django.db import models
from django.conf import settings


class BlogPost(models.Model):
    """
    A blog post (article) about beauty tips, tutorials, etc.
    """
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=270, unique=True)
    excerpt = models.TextField(max_length=300, blank=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='blog_posts',
    )
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title
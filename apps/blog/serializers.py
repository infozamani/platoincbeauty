from rest_framework import serializers
from .models import BlogPost


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id', 'name', 'slug')


class BlogPostSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = BlogPost
        fields = (
            'id', 'title', 'slug', 'author', 'author_name', 'category',
            'excerpt', 'content', 'cover_image', 'is_published',
            'published_at', 'created_at', 'updated_at',
        )
        read_only_fields = ('id', 'slug', 'author', 'created_at', 'updated_at')


class BlogPostListSerializer(serializers.ModelSerializer):
    """نسخه سبک برای لیست"""
    category = BlogCategorySerializer(read_only=True)
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'slug', 'author_name', 'category', 'excerpt', 'cover_image', 'published_at')
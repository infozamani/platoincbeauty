from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def blog_list(request):
    """
    Display published blog posts.
    """
    posts = BlogPost.objects.filter(is_published=True)
    return render(request, 'blog/list.html', {'posts': posts})


def blog_detail(request, slug):
    """
    Display a single blog post by slug.
    """
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'blog/detail.html', {'post': post})
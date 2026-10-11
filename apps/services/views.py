from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceCategory


def service_list(request):
    """
    Display all active services with optional filtering by gender and category.
    Query params:
        - gender: 'male' | 'female' | 'unisex' (optional)
        - category: category slug (optional)
    """
    services = Service.objects.filter(is_active=True)

    # Filter by gender if provided in the query string
    gender = request.GET.get('gender')
    if gender in ['male', 'female', 'unisex']:
        services = services.filter(gender=gender)

    # Filter by category slug if provided
    category_slug = request.GET.get('category')
    if category_slug:
        services = services.filter(category__slug=category_slug)

    context = {
        'services': services,
        'categories': ServiceCategory.objects.all(),
        'selected_gender': gender,
        'selected_category': category_slug,
    }
    return render(request, 'services/list.html', context)


def service_detail(request, slug):
    """
    Display a single service by its slug.
    """
    service = get_object_or_404(Service, slug=slug, is_active=True)
    context = {
        'service': service,
    }
    return render(request, 'services/detail.html', context)
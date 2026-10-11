from django.shortcuts import render
from .models import GalleryItem


def gallery_list(request):
    """
    Display all active gallery items.
    Optional filter: ?category=hair or ?gender=female
    """
    items = GalleryItem.objects.filter(is_active=True)

    category = request.GET.get('category')
    if category:
        items = items.filter(category=category)

    gender = request.GET.get('gender')
    if gender:
        items = items.filter(gender=gender)

    return render(request, 'gallery/list.html', {
        'items': items,
        'selected_category': category,
        'selected_gender': gender,
    })
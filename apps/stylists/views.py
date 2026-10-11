from django.shortcuts import render, get_object_or_404
from .models import Stylist


def stylist_list(request):
    """
    Display all active stylists.
    Optional filter: ?gender=male|female|unisex
    """
    stylists = Stylist.objects.filter(is_active=True)
    return render(request, 'stylists/list.html', {'stylists': stylists})


def stylist_detail(request, slug):
    """
    Display a single stylist's profile, their specialties, and approved reviews.
    """
    stylist = get_object_or_404(Stylist, slug=slug, is_active=True)
    reviews = stylist.reviews.filter(is_approved=True)

    context = {
        'stylist': stylist,
        'reviews': reviews,
    }
    return render(request, 'stylists/detail.html', context)
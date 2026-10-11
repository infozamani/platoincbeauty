from django.shortcuts import render
from apps.services.models import Service


def home(request):
    """
    Render the home page with a few featured services.
    Only active services are shown to the public.
    """
    # Fetch the first 3 active services to display on the home page
    featured_services = Service.objects.filter(is_active=True)[:3]

    context = {
        'featured_services': featured_services,
    }
    return render(request, 'core/home.html', context)


def contact(request):
    """
    Render the contact page.
    A simple static page with address, phone, and a contact form placeholder.
    """
    return render(request, 'core/contact.html')
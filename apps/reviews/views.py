from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review
from apps.stylists.models import Stylist


def review_create(request):
    """
    Allow a customer to submit a review for a stylist.
    Reviews require admin approval before appearing publicly.
    """
    if request.method == 'POST':
        stylist_id = request.POST.get('stylist')
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '')

        if stylist_id and name and rating:
            stylist = Stylist.objects.get(id=stylist_id)
            Review.objects.create(
                customer_name=name,
                stylist=stylist,
                rating=rating,
                comment=comment,
            )
            messages.success(request, 'Thank you! Your review is pending approval.')
            return redirect('reviews:create')

    return render(request, 'reviews/create.html', {'stylists': Stylist.objects.filter(is_active=True)})
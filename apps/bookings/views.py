from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from .models import Booking
from apps.services.models import Service
from apps.stylists.models import Stylist


def booking_create(request):
    """
    Multi-step booking form.
    Step 1: Choose service (passed as ?service=ID)
    Step 2: Choose stylist (passed as ?stylist=ID)
    Step 3: Choose date & time
    Step 4: Enter contact info
    """
    services = Service.objects.filter(is_active=True)
    stylists = Stylist.objects.filter(is_active=True)

    if request.method == 'POST':
        service_id = request.POST.get('service')
        stylist_id = request.POST.get('stylist')
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email', '')

        # Validate all required fields
        if not all([service_id, stylist_id, date_str, time_str, name, phone]):
            messages.error(request, 'Please fill in all required fields.')
            return redirect('bookings:create')

        service = get_object_or_404(Service, id=service_id)
        stylist = get_object_or_404(Stylist, id=stylist_id)

        # Build datetime objects
        start_dt = timezone.make_aware(
            datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        )
        end_dt = start_dt + timedelta(minutes=service.duration_minutes)

        # Check for conflict
        conflict = Booking.objects.filter(
            stylist=stylist,
            start_datetime__lt=end_dt,
            end_datetime__gt=start_dt,
            status__in=['pending', 'confirmed'],
        ).exists()

        if conflict:
            messages.error(request, 'This time slot is already booked. Please choose another.')
            return redirect('bookings:create')

        # Create booking
        Booking.objects.create(
            customer_name=name,
            customer_phone=phone,
            customer_email=email,
            service=service,
            stylist=stylist,
            start_datetime=start_dt,
            end_datetime=end_dt,
        )

        messages.success(request, 'Your booking was submitted! We will contact you to confirm.')
        return redirect('bookings:success')

    context = {
        'services': services,
        'stylists': stylists,
        'preselected_service': request.GET.get('service'),
        'preselected_stylist': request.GET.get('stylist'),
    }
    return render(request, 'bookings/create.html', context)


def booking_success(request):
    """
    Success page shown after a booking is created.
    """
    return render(request, 'bookings/success.html')


def booking_lookup(request):
    """
    Allow a customer to look up their booking using phone + last 6 digits.
    No account required.
    """
    bookings = None
    if request.method == 'POST':
        phone = request.POST.get('phone', '').strip()
        last_digits = request.POST.get('last_digits', '').strip()

        if phone and last_digits and phone.endswith(last_digits):
            bookings = Booking.objects.filter(customer_phone=phone).order_by('-start_datetime')

    return render(request, 'bookings/lookup.html', {'bookings': bookings})


def api_available_slots(request, stylist_id):
    """
    JSON endpoint: return available time slots for a given stylist on a given date.
    Query params: date=YYYY-MM-DD
    """
    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse({'error': 'date is required'}, status=400)

    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return JsonResponse({'error': 'Invalid date format'}, status=400)

    stylist = get_object_or_404(Stylist, id=stylist_id, is_active=True)

    # Assume working hours 9:00–18:00 for now
    slots = []
    for hour in range(9, 18):
        for minute in [0, 30]:
            slot_start = timezone.make_aware(datetime.combine(target_date, datetime.min.time()).replace(hour=hour, minute=minute))
            slot_end = slot_start + timedelta(minutes=30)

            conflict = Booking.objects.filter(
                stylist=stylist,
                start_datetime__lt=slot_end,
                end_datetime__gt=slot_start,
                status__in=['pending', 'confirmed'],
            ).exists()

            if not conflict:
                slots.append(slot_start.strftime("%H:%M"))

    return JsonResponse({'slots': slots})
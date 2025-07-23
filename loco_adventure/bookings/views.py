from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from adventures.models import Adventure
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import generate_ticket_pdf, send_ticket_email

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

@login_required
def create_booking(request, adventure_id):
    from django.contrib import messages
    adventure = get_object_or_404(Adventure, pk=adventure_id)
    if not adventure.online_booking:
        # If online booking is not allowed, redirect or show error
        messages.error(request, "Online booking is not available for this adventure.")
        return redirect('user-dashboard')
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        total_price = adventure.price * quantity
        booking = Booking.objects.create(
            user=request.user,
            adventure=adventure,
            tickets=quantity,
            total_price=total_price,
            status='C'  # Confirmed
        )
        # Generate PDF ticket
        pdf_bytes = generate_ticket_pdf(booking)
        # Send email with PDF attached
        try:
            send_ticket_email(request.user.email, pdf_bytes, booking)
            messages.success(request, "Booking successful! Ticket has been sent to your email.")
        except Exception as e:
            messages.error(request, f"Booking successful but failed to send ticket email: {e}")
        return redirect('bookings:booking-detail', pk=booking.pk)
    return render(request, 'core/booking.html', {'adventure': adventure, 'quantity': 1, 'total_amount': adventure.price})

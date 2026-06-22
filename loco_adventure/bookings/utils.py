import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.core.mail import EmailMessage
from django.conf import settings

def generate_ticket_pdf(booking):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    p.setFont("Helvetica-Bold", 20)
    p.drawString(72, height - 72, "LocoAdventure Ticket")

    p.setFont("Helvetica", 12)
    p.drawString(72, height - 120, f"Booking ID: {booking.id}")
    p.drawString(72, height - 140, f"User: {booking.user.username} ({booking.user.email})")
    p.drawString(72, height - 160, f"Adventure: {booking.adventure.title}")
    p.drawString(72, height - 180, f"Tickets: {booking.tickets}")
    p.drawString(72, height - 200, f"Total Price: ₹{booking.total_price:.2f}")
    p.drawString(72, height - 220, f"Booking Date: {booking.booking_date.strftime('%Y-%m-%d %H:%M:%S')}")

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    return pdf

import logging

def send_ticket_email(to_email, pdf_bytes, booking):
    subject = f"LocoAdventure Ticket Confirmation - Booking #{booking.id}"
    body = f"Dear {booking.user.username},\n\nThank you for your booking. Please find your ticket attached.\n\nEnjoy your adventure!\n\nBest regards,\nLocoAdventure Team"
    email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [to_email])
    email.attach(f"ticket_booking_{booking.id}.pdf", pdf_bytes, 'application/pdf')
    try:
        email.send()
        logging.info(f"Ticket email sent successfully to {to_email} for booking {booking.id}")
    except Exception as e:
        logging.error(f"Failed to send ticket email to {to_email} for booking {booking.id}: {e}")

import os

print("EMAIL_HOST_USER:", os.getenv("EMAIL_HOST_USER"))
print("PASSWORD EXISTS:", bool(os.getenv("EMAIL_HOST_PASSWORD")))
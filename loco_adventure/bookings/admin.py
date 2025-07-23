from django.contrib import admin
from .models import *

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'adventure', 'status', 'booking_date')
    list_filter = ('status', 'booking_date')

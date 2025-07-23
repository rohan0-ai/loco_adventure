from django.contrib import admin
from .models import *

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'business_name', 'verified', 'rating')

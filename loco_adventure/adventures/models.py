from django.db import models
from vendors.models import Vendor

class Adventure(models.Model):
    TYPES = [
        ('IN', 'Indoor'),
        ('OUT', 'Outdoor'),
        ('EVENT', 'Event')
    ]
    
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.PositiveIntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    adventure_type = models.CharField(max_length=5, choices=TYPES)
    address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    online_booking = models.BooleanField(default=False)
    image = models.ImageField(upload_to='adventure_images/', blank=True, null=True)

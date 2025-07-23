from django.db import models
from core.models import User

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    rating = models.FloatField(default=0.0)

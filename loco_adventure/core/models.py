from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('C', 'Customer'),
        ('V', 'Vendor'),
    )
    phone = models.CharField(max_length=15)
    user_type = models.CharField(max_length=1, choices=USER_TYPES)
    profile_pic = models.ImageField(upload_to='profiles/', null=True)

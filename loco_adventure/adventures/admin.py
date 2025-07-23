from django.contrib import admin
from .models import *

@admin.register(Adventure)
class AdventureAdmin(admin.ModelAdmin):
    list_display = ('title', 'vendor', 'price', 'adventure_type')

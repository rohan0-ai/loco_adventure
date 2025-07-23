from django.urls import path
from . import views

app_name = 'vendors'

urlpatterns = [
    path('register/', views.vendor_registration, name='vendor-register'),
    path('login/', views.vendor_login, name='vendor-login'),
    path('logout/', views.vendor_logout, name='vendor-logout'),
    path('dashboard/', views.vendor_dashboard, name='vendor-dashboard'),
    path('edit-adventure/<int:adventure_id>/', views.edit_adventure, name='edit-adventure'),
]

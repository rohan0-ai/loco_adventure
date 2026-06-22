from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.booking_list, name='booking-list'),
    path('create/<int:adventure_id>/', views.create_booking, name='create-booking'),
    path('<int:pk>/', views.booking_detail, name='booking-detail'),
    path(
        "download-ticket/<int:booking_id>/",
        views.download_ticket,
        name="download_ticket",
    ),
]

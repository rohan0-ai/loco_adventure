from django.urls import path
from . import views

app_name = 'adventures'

urlpatterns = [
    path('', views.adventure_list, name='adventure-list'),
    path('<int:pk>/', views.adventure_detail, name='adventure-detail'),
]

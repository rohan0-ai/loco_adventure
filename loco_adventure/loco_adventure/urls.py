"""
URL configuration for loco_adventure project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('register/', user_registration, name='user-register'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('dashboard/', user_dashboard, name='user-dashboard'),
    path('book/<int:adventure_id>/', booking, name='booking'),
    path('load-more-adventures/', load_more_adventures, name='load-more-adventures'),

    path('adventures/', include('adventures.urls', namespace='adventures')),
    path('bookings/', include('bookings.urls', namespace='bookings')),
    path('vendor/', include('vendors.urls', namespace='vendors')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

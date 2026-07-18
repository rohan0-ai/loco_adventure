from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdventureViewSet

router = DefaultRouter()
router.register("adventures", AdventureViewSet, basename="adventure")

urlpatterns = [
    path("", include(router.urls)),
]
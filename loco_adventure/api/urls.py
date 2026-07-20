from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import AdventureViewSet, NearbyPlacesView

router = DefaultRouter()
router.register("adventures", AdventureViewSet, basename="adventure")

urlpatterns = [
    path("", include(router.urls)),
    path("nearby/", NearbyPlacesView.as_view(), name="nearby"),
]
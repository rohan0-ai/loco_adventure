from rest_framework import viewsets
from adventures.models import Adventure
from .serializers import AdventureSerializer


class AdventureViewSet(viewsets.ModelViewSet):
    queryset = Adventure.objects.all()
    serializer_class = AdventureSerializer
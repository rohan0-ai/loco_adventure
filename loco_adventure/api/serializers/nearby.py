from rest_framework import serializers

from .place import PlaceSerializer


class NearbyResponseSerializer(serializers.Serializer):
    count = serializers.IntegerField()

    results = PlaceSerializer(many=True)
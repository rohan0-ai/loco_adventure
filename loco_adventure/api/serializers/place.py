from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lng = serializers.FloatField()

    address = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        required=False,
    )


class MediaSerializer(serializers.Serializer):
    image = serializers.URLField(
        allow_null=True,
        required=False,
    )

class DistanceSerializer(serializers.Serializer):
    meters = serializers.IntegerField()
    display = serializers.CharField()

class PlaceSerializer(serializers.Serializer):
    id = serializers.CharField()

    name = serializers.CharField()

    category = serializers.CharField()

    distance = DistanceSerializer()

    location = LocationSerializer(required=True)

    media = MediaSerializer(required=True)

    summary = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        required=False,
    )

    source = serializers.CharField()

class ExternalLinksSerializer(serializers.Serializer):
    opentripmap = serializers.URLField(allow_null=True)

class PlaceDetailSerializer(serializers.Serializer):

    id = serializers.CharField()

    name = serializers.CharField()

    category = serializers.CharField(allow_null=True)

    summary = serializers.CharField(allow_null=True)

    address = LocationSerializer(required=True)

    media = MediaSerializer(required=True)

    rating = serializers.CharField(allow_null=True)

    external_links = ExternalLinksSerializer()
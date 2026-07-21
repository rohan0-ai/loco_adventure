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


class PlaceSerializer(serializers.Serializer):
    id = serializers.CharField()

    name = serializers.CharField()

    category = serializers.CharField()

    distance = serializers.IntegerField()

    location = LocationSerializer(required=True)

    media = MediaSerializer(required=True)

    summary = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        required=False,
    )

    source = serializers.CharField()
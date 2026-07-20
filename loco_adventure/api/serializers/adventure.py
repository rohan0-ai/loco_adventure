from rest_framework import serializers
from adventures.models import Adventure


class AdventureSerializer(serializers.ModelSerializer):
    vendor = serializers.CharField(source="vendor.business_name", read_only=True)
    adventure_type = serializers.CharField(
        source="get_adventure_type_display",
        read_only=True
    )

    class Meta:
        model = Adventure
        fields = [
            "id",
            "title",
            "vendor",
            "price",
            "capacity",
            "address",
            "latitude",
            "longitude",
            "description",
            "image",
            "adventure_type",
            "online_booking",
        ]
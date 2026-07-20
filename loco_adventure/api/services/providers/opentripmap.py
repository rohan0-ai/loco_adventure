import os
import requests
from django.conf import settings

API_KEY = settings.OPENTRIPMAP_API_KEY

BASE_URL = "https://api.opentripmap.com/0.1/en/places/radius"


def get_nearby_places(lat, lon, radius=5000, limit=10):
    """
    Fetch nearby places from OpenTripMap.

    Args:
        lat (float): Latitude
        lon (float): Longitude
        radius (int): Search radius in meters
        limit (int): Maximum number of places

    Returns:
        dict: JSON response from OpenTripMap
    """

    params = {
        "radius": radius,
        "lon": lon,
        "lat": lat,
        "limit": limit,
        "apikey": API_KEY,
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    return response.json()
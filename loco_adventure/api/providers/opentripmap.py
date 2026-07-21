import os
import requests
from django.conf import settings

API_KEY = settings.OPENTRIPMAP_API_KEY

BASE_URL = "https://api.opentripmap.com/0.1/en"

def _make_request(endpoint, params=None):
    url = f"{BASE_URL}{endpoint}"

    response = requests.get(
        url,
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()


def get_nearby_places(lat, lon, radius=5000, limit=10, offset=0):

    params = {
        "radius": radius,
        "lon": lon,
        "lat": lat,
        "limit": limit,
        "offset": offset,
        "apikey": API_KEY,
    }

    return _make_request(
        "/places/radius",
        params=params,
    )

def get_place_details(xid):
    return _make_request(
        f"/places/xid/{xid}",
        params={"apikey": API_KEY},
    )
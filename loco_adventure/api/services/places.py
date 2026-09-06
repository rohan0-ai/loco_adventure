from api.providers import get_nearby_places
from api.formatters import format_nearby_places

from api.providers.opentripmap import get_place_details as provider_get_place_details
from api.formatters import format_place_details, format_place_full_details

import logging

logger = logging.getLogger(__name__)


MAX_ATTEMPTS = 5


def search_nearby_places(lat, lon, radius=5000, limit=10):

    places = []
    offset = 0
    attempts = 0

    while len(places) < limit and attempts < MAX_ATTEMPTS:

        raw_data = get_nearby_places(
            lat=lat,
            lon=lon,
            radius=radius,
            limit=limit,
            offset=offset,
        )

        features = raw_data.get("features", [])

        if not features:
            break

        formatted = format_nearby_places(raw_data)


        places.extend(formatted)

        offset += limit
        attempts += 1

    rich_places = []

    for place in places[:limit]:
        rich_places.append(
            enrich_place(place)
    )

    return rich_places


def enrich_place(place):

    try:
        raw = provider_get_place_details(place["id"])
        details = format_place_details(raw)

    except Exception as e:
        logger.exception(
            "Failed to enrich place %s",
            place["id"],
        )
        
        details = {
            "summary": "",
            "media": {"image": None},
            "location": {"address": ""},
        }

    return {
    "id": place["id"],
    "name": place["name"],
    "category": place["category"],
    "distance": place["distance"],

    "location": {
        "lat": place["latitude"],
        "lng": place["longitude"],
        "address": details["location"]["address"],
    },

    "media": details["media"],

    "summary": details["summary"],

    "source": place["source"],
}

def get_place_details(xid):
    raw_data = provider_get_place_details(xid)
    formatted_data = format_place_full_details(raw_data)
    return formatted_data
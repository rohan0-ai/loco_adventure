from .providers.opentripmap import get_nearby_places
from .formatter import format_opentripmap_places


def search_nearby_places(lat, lon, radius=5000, limit=10):

    raw_data = get_nearby_places(
        lat=lat,
        lon=lon,
        radius=radius,
        limit=limit,
    )

    return format_opentripmap_places(raw_data)
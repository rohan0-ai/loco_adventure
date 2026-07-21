from .category_mapper import map_category


def format_nearby_places(raw_data):
    """
    Convert OpenTripMap nearby response into our application's format.
    """

    formatted_places = []

    for feature in raw_data.get("features", []):

        properties = feature.get("properties", {})
        geometry = feature.get("geometry", {})

        name = properties.get("name")

        if not name:
            continue

        coordinates = geometry.get("coordinates", [None, None])

        formatted_places.append({
            "id": properties.get("xid"),
            "name": name,
            "distance": round(properties.get("dist", 0)),
            "latitude": coordinates[1],
            "longitude": coordinates[0],
            "category": map_category(properties.get("kinds", "")),
            "source": "opentripmap",
        })

    return formatted_places
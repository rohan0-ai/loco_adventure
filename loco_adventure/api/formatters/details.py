from .category_mapper import map_category


def format_place_details(raw_data):

    return {
        "summary": build_summary(raw_data),

        "media": {
            "image": build_image(raw_data),
        },

        "location": {
            "address": build_address(
                raw_data.get("address", {})
            )
        }
    }

def build_address(address):
    """
    Convert OpenTripMap address object into a readable string.
    """

    parts = [
        address.get("road"),
        address.get("suburb"),
        address.get("city"),
        address.get("state"),
    ]

    return ", ".join(part for part in parts if part)

def build_summary(raw_data, limit=180):

    summary = (
        raw_data.get("wikipedia_extracts", {})
        .get("text", "")
        .strip()
    )

    if len(summary) > limit:
        summary = summary[:limit].rstrip() + "..."

    return summary

def build_image(raw_data):

    preview = raw_data.get("preview", {})

    return preview.get("source")
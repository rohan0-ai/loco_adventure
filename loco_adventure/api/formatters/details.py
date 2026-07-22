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

def normalize_image_url(url):
    """
    Convert Wikimedia thumbnail URLs to the original image URL.

    Example:
    https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/image.jpg/266px-image.jpg to 
        
    https://upload.wikimedia.org/wikipedia/commons/0/07/image.jpg
    """

    if not url:
        return None

    if "upload.wikimedia.org" not in url or "/thumb/" not in url:
        return url

    parts = url.split("/")

    parts.remove("thumb")

    parts.pop()

    return "/".join(parts)

def build_image(raw_data):
    preview = raw_data.get("preview", {})
    image_url = preview.get("source")

    return normalize_image_url(image_url)

def format_distance(distance):
    """
    Format distance for display while preserving the raw value.
    """

    if distance is None:
        return None

    if distance < 1000:
        display = f"{int(distance)} m"
    else:
        display = f"{distance / 1000:.1f} km"

    return {
        "meters": int(distance),
        "display": display,
    }
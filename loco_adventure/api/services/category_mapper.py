CATEGORY_MAPPING = {
    "historic": "Historical",
    "museums": "Museum",
    "cultural": "Cultural",
    "parks": "Park",
    "natural": "Nature",
    "religion": "Religious",
    "architecture": "Architecture",
    "monuments_and_memorials": "Monument",
    "tourist_object": "Tourist Attraction",
}


def map_category(kinds: str) -> str:
    """
    Convert OpenTripMap kinds into user-friendly categories.
    """

    if not kinds:
        return "Other"

    for kind in kinds.split(","):
        if kind in CATEGORY_MAPPING:
            return CATEGORY_MAPPING[kind]

    return "Other"
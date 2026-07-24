export async function fetchPlaceDetails(xid) {

    console.log("4. Fetching place details");

    const response = await fetch(`/api/places/${xid}/`);

    if (!response.ok) {
        throw new Error("Failed to fetch place details.");
    }

    return await response.json();

}
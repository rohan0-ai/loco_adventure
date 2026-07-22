async function fetchNearbyPlaces(latitude, longitude) {

    console.log("8. Inside fetchNearbyPlaces");

    const response = await fetch(
        `/api/nearby/?lat=${latitude}&lng=${longitude}`
    );

    console.log("9. Response:", response);

    if (!response.ok) {
        throw new Error("Failed to fetch nearby places.");
    }

    return await response.json();
}

export { fetchNearbyPlaces };
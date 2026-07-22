document.addEventListener("DOMContentLoaded", () => {
    console.log("1. DOM loaded");
    getUserLocation();
});

function getUserLocation() {

    console.log("2. Getting location");

    if (!navigator.geolocation) {
        console.error("Geolocation is not supported.");
        return;
    }

    navigator.geolocation.getCurrentPosition(
        handleLocationSuccess,
        handleLocationError
    );
}

function handleLocationSuccess(position) {

    console.log("3. Location received");

    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    console.log(latitude, longitude);

    loadNearbyPlaces(latitude, longitude);
}

function handleLocationError(error) {
    console.error("Location error:", error);
}

async function loadNearbyPlaces(latitude, longitude) {

    console.log("4. loadNearbyPlaces called");

    try {

        console.log("5. Calling API...");

        const places = await fetchNearbyPlaces(latitude, longitude);

        renderNearbyPlaces(places);

    } catch (error) {

        console.error("7. Error:", error);

    }

}

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

function renderNearbyPlaces(data) {

    const container = document.getElementById("nearby-container");

    container.innerHTML = "";

    data.results.forEach(place => {

        const card = createPlaceCard(place);

        container.appendChild(card);

    });

}

function createPlaceCard(place) {

    const card = document.createElement("div");

    card.className =
        "adventure-card bg-white rounded-xl overflow-hidden";

    card.innerHTML = buildPlaceCardTemplate(place);

    return card;

}

function buildPlaceCardTemplate(place) {

    const image = place.media.image || "/static/Images/default.jpg";

    return `
        <img src="${image}"
             alt="${place.name}"
             class="w-full h-48 object-cover">

        <div class="p-6">

            <div class="flex justify-between items-start mb-4">

                <h3 class="text-xl font-bold text-purple-600">
                    ${place.name}
                </h3>

                <span
                    class="bg-yellow-100 text-yellow-800 px-3 py-1 rounded-full text-sm">

                    ${place.distance.display}

                </span>

            </div>

            <p class="text-gray-600 mb-2 font-semibold">

                📍 ${place.location.address}

            </p>

            <p class="text-gray-600 mb-4">

                ${place.summary}

            </p>

            <button
                class="bg-purple-500 hover:bg-purple-600 text-white px-6 py-2 rounded-full">

                Explore

            </button>

        </div>
    `;
}
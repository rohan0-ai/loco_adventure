import { getUserLocation } from "./location.js";
import { fetchNearbyPlaces } from "./api.js";
import { renderNearbyPlaces } from "./renderer.js";

document.addEventListener("DOMContentLoaded", async () => {

    console.log("1. DOM loaded");

    try {

        const { latitude, longitude } = await getUserLocation();

        await loadNearbyPlaces(latitude, longitude);

    } catch (error) {

        console.error(error);

    }

});

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
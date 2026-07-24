import { fetchPlaceDetails } from "./api.js";
import { renderPlaceDetails } from "./renderer.js";

document.addEventListener("DOMContentLoaded", async () => {

    console.log("1. Place page loaded");

    const container = document.getElementById("place-detail");
    const xid = container.dataset.xid;

    console.log("2. XID:", xid);

    await loadPlaceDetails(xid);

});

async function loadPlaceDetails(xid) {

    console.log("3. Loading place details");

    try {

        const place = await fetchPlaceDetails(xid);

        renderPlaceDetails(place);

    } catch (error) {

        console.error("Failed to load place:", error);

    }

}
import { buildPlaceDetailsTemplate } from "./templates.js";

export function renderPlaceDetails(place) {

    console.log("5. Rendering place");

    const container = document.getElementById("place-detail");

    container.innerHTML = buildPlaceDetailsTemplate(place);

}
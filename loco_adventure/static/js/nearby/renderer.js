import { buildPlaceCardTemplate } from "./templates.js";

export function renderNearbyPlaces(data) {

    const container = document.getElementById("nearby-container");

    container.innerHTML = "";

    data.results.forEach(place => {

        const card = createNearbyCard(place);

        container.appendChild(card);

    });

}

export function createNearbyCard(place) {

    const card = document.createElement("div");

    card.innerHTML = buildPlaceCardTemplate(place);

    const exploreButton = card.querySelector(".explore-btn");

    exploreButton.addEventListener("click", () => {
        window.location.href = `/place/${place.id}/`;
    });

    return card;
}
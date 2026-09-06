export function buildPlaceDetailsTemplate(place) {

    console.log("PLACE DETAILS:", place);
    console.log("ADDRESS:", place.address);

    return `
        <h1 class="text-4xl font-bold mb-6">
            ${place.name}
        </h1>

        <p class="mb-4">
            <strong>Category:</strong>
            ${place.category ?? "N/A"}
        </p>

        <p class="mb-4">
            <strong>Summary:</strong>
            ${place.summary ?? "No description available."}
        </p>

        <p class="mb-4">
            <strong>Address:</strong>
            ${place.address?.address ?? "Unknown"}
        </p>
    `;
}
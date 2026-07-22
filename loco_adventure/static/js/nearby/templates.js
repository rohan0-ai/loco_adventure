export function buildPlaceCardTemplate(place) {

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
                class="bg-purple-500 hover:bg-purple-600 text-white px-6 py-2 rounded-full explore-btn"
                data-xid="${place.id}">

                Explore

            </button>

        </div>
    `;
}
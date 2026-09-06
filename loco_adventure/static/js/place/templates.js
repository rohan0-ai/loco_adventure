export function buildPlaceDetailsTemplate(place) {

    const mapsUrl = place.address?.lat && place.address?.lng
        ? `https://www.google.com/maps/dir/?api=1&destination=${place.address.lat},${place.address.lng}`
        : null;

    return `
        <div class="max-w-6xl mx-auto">

            <!-- Title -->
            <h1 class="text-4xl md:text-5xl font-bold text-purple-600 mb-8">
                ${place.name}
            </h1>

            <!-- Main Content -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-12">

                <!-- Image -->
                <div>
                    ${place.media?.image
            ? `
                                <img
                                    src="${place.media.image}"
                                    alt="${place.name}"
                                    class="w-full h-[350px] md:h-[450px] object-cover rounded-xl shadow-lg"
                                >
                            `
            : `
                                <div
                                    class="w-full h-[350px] md:h-[450px] bg-gray-200 rounded-xl
                                           flex items-center justify-center text-gray-500"
                                >
                                    No image available
                                </div>
                            `
        }
                </div>

                <!-- Details -->
                <div class="flex flex-col">

                    <!-- Category -->
                    <p class="text-lg mb-5">
                        <strong class="text-gray-800">Category:</strong>
                        <span class="text-gray-600">
                            ${place.category ?? "N/A"}
                        </span>
                    </p>

                    <!-- Summary -->
                    <div class="mb-8">
                        <h2 class="text-xl font-bold text-purple-600 mb-3">
                            About this place
                        </h2>

                        <p class="text-gray-700 leading-relaxed text-lg">
                            ${place.summary ?? "No description available."}
                        </p>
                    </div>

                    <!-- Address -->
                    <div class="mb-6">
                        <h2 class="text-xl font-bold text-purple-600 mb-3">
                            Location
                        </h2>

                        <p class="text-gray-700 leading-relaxed">
                            ${place.address?.address
        ?? "Address not available"
        }
                        </p>
                    </div>

                    <!-- Rating -->
                    ${place.rating
            ? `
                                <p class="text-lg text-gray-700 mb-6">
                                    <strong class="text-gray-800">Rating:</strong>
                                    ⭐ ${place.rating}
                                </p>
                            `
            : ""
        }

                    <!-- Buttons -->
                    <div class="mt-auto flex flex-wrap gap-4">

                        ${mapsUrl
            ? `
                                    <a
                                        href="${mapsUrl}"
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        class="inline-flex items-center justify-center
                                               bg-purple-600 hover:bg-purple-700
                                               text-white px-6 py-3 rounded-full
                                               font-semibold transition shadow-md
                                               hover:shadow-lg"
                                    >
                                        📍 Get Directions
                                    </a>
                                `
            : ""
        }

                        <a
                            href="/dashboard/"
                            class="inline-flex items-center justify-center
                                   bg-gray-200 hover:bg-gray-300
                                   text-gray-800 px-6 py-3 rounded-full
                                   font-semibold transition"
                        >
                            ← Back to Dashboard
                        </a>

                    </div>

                </div>

            </div>

        </div>
    `;
}
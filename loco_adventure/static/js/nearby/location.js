export function getUserLocation() {

    console.log("2. Getting location");

    if (!navigator.geolocation) {
        return Promise.reject(
            new Error("Geolocation is not supported.")
        );
    }

    return new Promise((resolve, reject) => {

        navigator.geolocation.getCurrentPosition(

            (position) => {

                console.log("3. Location received");

                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;

                console.log(latitude, longitude);

                resolve({
                    latitude,
                    longitude,
                });

            },

            (error) => {

                console.error("Location error:", error);
                reject(error);

            }

        );

    });

}
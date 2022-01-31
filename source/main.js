// Elements on page
const main = document.getElementById ('main');

/**
 * Function: Grab IP address to gather locstion/weather data
 * Temporary, runs on a page load
 */
window.addEventListener ("load", () => {
    console.log ("page loaded");

    fetch ('http://ip-api.com/json')
        .then (res => res.json())
        .then (response => {
            main.textContent = "Country: " + response.country + " | City: " + response.city + " | Timezone: " + response.timezone;
            console.log ("Country: ", response.country);
            console.log ("City: ", response.city);
            console.log ("Timezone: ", response.timezone);
            console.log ("Lat (", response.lat, ") Lon (", response.lon, ")");
        })
        .catch ((data, status) => {
            console.log('Request failed');
        })
});



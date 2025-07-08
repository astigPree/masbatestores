
var main_holder = document.getElementById('main-holder');


var DEFAULT_LOCATION = [12.371461264522235, 123.62375723675078]

// Define tile layers
var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
});

var satellite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
  attribution: 'Tiles © Esri'
});

// Initialize the map with satellite as default
var map = L.map('map', {
  center: DEFAULT_LOCATION,
  zoom: 15,
  zoomControl: false,
  layers: [satellite] // default layer
});

 
var customIcon = L.icon({
    iconUrl: '/static/assets/guest-current-location.svg', // Replace with your image path
    iconSize: [24, 32],       // Size of the icon
    iconAnchor: [16, 32],     // Point of the icon which corresponds to marker location
    popupAnchor: [0, -32]     // Where the popup opens relative to the iconAnchor
});
var openStoreIcon = L.icon({
    iconUrl: '/static/assets/guest-green-store.svg', // Replace with your image path
    iconSize: [32, 32],       // Size of the icon
    iconAnchor: [16, 32],     // Point of the icon which corresponds to marker location
    popupAnchor: [0, -32]     // Where the popup opens relative to the iconAnchor
});
var closeStoreIcon = L.icon({
    iconUrl: '/static/assets/guest-gray-store.svg', // Replace with your image path
    iconSize: [32, 32],       // Size of the icon
    iconAnchor: [16, 32],     // Point of the icon which corresponds to marker location
    popupAnchor: [0, -32]     // Where the popup opens relative to the iconAnchor
});

 
var currentLayer = 'satellite'; 
function toggleMap() {
  if (currentLayer === 'satellite') {
    map.removeLayer(satellite);
    map.addLayer(street);
    currentLayer = 'street';
  } else {
    map.removeLayer(street);
    map.addLayer(satellite);
    currentLayer = 'satellite';
  }
}


var current_marker = null;
function getStoreNearMe(){
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
        var lat = position.coords.latitude;
        var lng = position.coords.longitude;

        // Center map on your location
        map.setView([lat, lng], 15);

        if (current_marker) {
            map.removeLayer(current_marker);
        }
        // Add a marker for current location
        current_marker = L.marker([lat, lng], {
            icon: customIcon
        }).addTo(map)
        .bindPopup('You are here!')
        .openPopup();
  
    }, function(error) {
        console.error("Error getting location: ", error);
    });
    } else {
        alert("Geolocation is not supported by this browser.");
    }

}



document.addEventListener("DOMContentLoaded", function() {  

  // Get the save session before that tell user view the term and condition
  var isviewedbefore = localStorage.getItem('isviewedbefore');
  if (!isviewedbefore) {
    localStorage.setItem('isviewedbefore', true);
    // main_holder.insertAdjacentHTML("afterbegin", term_and_conditions_dom());
  } else{
    getStoreNearMe();
    document.getElementById("near-me-button").addEventListener("click", getStoreNearMe);
    document.getElementById("map-button").addEventListener("click", toggleMap);
  }


})
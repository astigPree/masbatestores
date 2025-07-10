
var main_holder = document.getElementById('main-holder');


var DEFAULT_LOCATION = [12.371461264522235, 123.62375723675078]
var map = null; // Global variable to hold the map instance

// Define tile layers
var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
});

var satellite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
  attribution: 'Tiles © Esri'
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
var is_first_time_load = true;

function displayStores(stores){
  // Display the store list dom
  var storeList = document.getElementById('store-list-container');
  if (storeList) {
    // The store list is already displayed
    // Do nothing
    console.log('Store list is already displayed');
    return;
  }
  main_holder.insertAdjacentHTML("afterbegin", store_list_dom());

  setTimeout(() => {
    storeList = document.getElementById('store-list-container');
    const store_list_close_button = document.getElementById('close-store-list-button');

    const handleClose = function () {
      storeList.classList.remove('animate-in');
      storeList.classList.add('animate-out');

      storeList.addEventListener('animationend', function handleAnimationEnd() {
        storeList.remove();
        storeList.removeEventListener('animationend', handleAnimationEnd); 
        // ✅ Clean up this click listener too
        store_list_close_button.removeEventListener('click', handleClose);
      });
    };

    store_list_close_button.addEventListener('click', handleClose);
  }, 0);
}

function displayEmtpyStores(){
  // Display the store empty list dom
  var storeList = document.getElementById('store-empty-list-container');
  if (storeList) {
    // The store list is already displayed
    // Do nothing
    console.log('Store list is already displayed');
    return;
  }
  main_holder.insertAdjacentHTML("afterbegin", store_empty_list_dom());

  setTimeout(() => {
    storeList = document.getElementById('store-empty-list-container');
    const store_list_close_button = document.getElementById('store-empty-list-button');

    const handleClose = function () {
      storeList.classList.remove('animate-in');
      storeList.classList.add('animate-out');

      storeList.addEventListener('animationend', function handleAnimationEnd() {
        storeList.remove();
        storeList.removeEventListener('animationend', handleAnimationEnd); 
        // ✅ Clean up this click listener too
        store_list_close_button.removeEventListener('click', handleClose);
      });
    };

    store_list_close_button.addEventListener('click', handleClose);
  }, 0);

}

function getStoreNearMe(){
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
        var lat = position.coords.latitude;
        var lng = position.coords.longitude;
        
        if (!map) {
            // Initialize the map with satellite as default
            map = L.map('map', {
                center: [lat, lng],
                zoom: 15,
                zoomControl: false,
                layers: [satellite] // default layer
            });
          } else{
            map.setView([lat, lng], 15);
          }

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

        // If there is so many stores then display the store list
        // if (stores.length > 0) {
        // } else {
        stores = [232];
        // displayStores(stores);
        // }
        if (!is_first_time_load && stores.length > 0) {
            displayStores(stores);
        }

        // if there is no stores then display the empty store list
        if (stores.length === 0 && !is_first_time_load) {
            displayEmtpyStores();
        }
  
        is_first_time_load = false;
    }, function(error) {
        console.error("Error getting location: ", error);
        // Initialize the map with satellite as default
        map = L.map('map', {
          center: DEFAULT_LOCATION,
          zoom: 15,
          zoomControl: false,
          layers: [satellite] // default layer
        });

    });
    } else {
        alert("Geolocation is not supported by this browser.");
        map = L.map('map', {
          center: DEFAULT_LOCATION,
          zoom: 15,
          zoomControl: false,
          layers: [satellite] // default layer
        });

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
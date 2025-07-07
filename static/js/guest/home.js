// Define tile layers
var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
});

var satellite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
  attribution: 'Tiles © Esri'
});

// Initialize the map with satellite as default
var map = L.map('map', {
  center: [12.375325409266404, 123.63267841062742],
  zoom: 13,
  zoomControl: false,
  layers: [satellite] // default layer
});

// // Add marker
// L.marker([12.375325409266404, 123.63267841062742]).addTo(map)
//   .bindPopup('Hello from Masbate!')
//   .openPopup();


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
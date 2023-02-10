
var current_marker_position, current_accuracy;
var LatitDef = -7.8751223;
var LongiDef = 112.5109015;
var map_init = L.map('maparea').setView([LatitDef, LongiDef], 13);


L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { 
  scrollWheelZoom: true,
  maxZoom: 19,
  // attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map_init);


map_init.on('locationfound', onLocationFound);
map_init.on('locationerror', onLocationError);
map_init.on('click', onMapClick);
ShowMapArea();

// map_init.on('load', ShowMapArea);

function onMapClick(e) {

    $("#id_rkp_long").val(e.latlng.lng);
    $("#id_rkp_lat").val(e.latlng.lat);
   
    if (current_marker_position){
      map_init.removeLayer(current_marker_position);
    }

    current_marker_position = new L.marker(e.latlng).addTo(map_init)
    .bindPopup("Posisi anda berada di koordinat  <br>" + " Latitude : " + e.latlng.lat +  " Longitude : " + e.latlng.lng  ).openPopup();

    
    map_init.setView(e.latlng);
    // this.current_accuracy = L.circle(e.latlng, radius).addTo(map_init);
}


function onLocationFound(e) {
  
  if (current_marker_position){
    map_init.removeLayer(current_marker_position);
  }

    var radius = e.accuracy / 2;

    current_marker_position = new L.marker(e.latlng).addTo(map_init)
    .bindPopup("Posisi anda berada di koordinat  <br>" + " Latitude : " + e.latlng.lat +  " Longitude : " + e.latlng.lng  ).openPopup();

    map_init.setView(e.latlng);

  $("#id_rkp_long").val(e.latlng.lng);
  $("#id_rkp_lat").val(e.latlng.lat);
}

function onLocationError(e) {
  alert(e.message);
}

// wrap map.locate in a function    
function mycurrentposition() {

  if (current_marker_position){
    map_init.removeLayer(current_marker_position);
  }
  map_init.locate({setView: true, maxZoom: 19});
}



function ShowMapArea(e) {

    var Lng = $("#id_rkp_long").val();
    var Lat = $("#id_rkp_lat").val();
    if (Lat == ""){ Lat = LatitDef}
    if (Lng == ""){ Lng = LongiDef}

    if (current_marker_position){
      map_init.removeLayer(current_marker_position);
    }

    current_marker_position = new L.marker([Lat, Lng]).addTo(map_init)
    .bindPopup("Posisi anda berada di koordinat  <br>" + " Latitude : " + Lat +  " Longitude : " + Lng  ).openPopup();

    map_init.setView([Lat, Lng], 13);
  }

// $( document ).ready(function() {

  // ShowMapArea();// });

mapboxgl.accessToken = 'pk.eyJ1IjoieXVyaXlrb3JtaW4iLCJhIjoiY2xjdTZjMm1jMHJwZTNvbXg1cm1xMGh5ciJ9.uHPoJEdjly2KUEmc8YEOkw';

const map = new mapboxgl.Map({
container: 'map', // container ID
style: 'mapbox://styles/mapbox/streets-v12', // style URL
center: [41.612803, 41.632153], // starting position [lng, lat]
zoom: 16, // starting zoom
language: 'ru-RU'
});
map.addControl(new mapboxgl.FullscreenControl());
map.addControl(new mapboxgl.GeolocateControl({
    positionOptions: {
    enableHighAccuracy: true
    },
    trackUserLocation: true,
    showUserHeading: true
}));
map.addControl(new mapboxgl.NavigationControl());
var markers = {};
var popups = {};


function set_popup (id, text) {
    popups[id] = new mapboxgl.Popup(
        {
            offset: 25,
            closeButton: false,
            closeOnClick: true,
        },
    ).setText(text)
}
function set_marker (id, lng, lat) {
    markers[id] = new mapboxgl.Marker()
        .setPopup(popups[id])
        .setLngLat([lng, lat])
        .addTo(map);

    // if (id == 11){
    //     // markers[id].icon({'marker-color': 'red'})
    //     alert(markers[id].properties)
    // }
}
function move_marker (event) {
    var coordinates = event.lngLat;
    var id = document.getElementById("id").value
    if (id in markers ){
        markers[id].setLngLat(coordinates).addTo(map);
    } else {
        set_marker(id, coordinates.lng, coordinates.lat);
    }
    document.getElementById("gps_point").setAttribute('value',"SRID=4326;POINT("+coordinates.lng.toString() +" " +coordinates.lat.toString()+')')
}

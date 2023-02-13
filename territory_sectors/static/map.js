mapboxgl.accessToken = 'pk.eyJ1IjoieXVyaXlrb3JtaW4iLCJhIjoiY2xjdTZjMm1jMHJwZTNvbXg1cm1xMGh5ciJ9.uHPoJEdjly2KUEmc8YEOkw';

//
// geocoder = new MapboxGeocoder({
//     accessToken:mapboxgl.accessToken,
//     mapboxgl:mapboxgl,
//     reverseGeocode:true,
// })

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
// mapboxgl.setRTLTextPlugin('https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-rtl-text/v0.2.3/mapbox-gl-rtl-text.js');
// map.addControl(new MapboxLanguage({defaultLanguage: 'ru'}));
var markers = {};
var popups = {};
var sectors = [];

// var sector_sources = {};


function set_popup (id, text) {
    popups[id] = new mapboxgl.Popup(
        {
            offset: 25,
            closeButton: false,
            closeOnClick: true,
        },
    ).setText(text)
}

function circle_text() {
    // const el = document.createElement('div');
    // el.style.width = `30px`;
    // el.style.height = `30px`;
    // // el.className = 'marker';
    // el.innerText= txt
    console.log(markers)

    map.addLayer({
                'id': 'poi-labels',
                'type': 'symbol',
                'source': 'markers',
                'layout': {
                    'text-field': ['get', 'description'],
                    'text-variable-anchor': ['top', 'bottom', 'left', 'right'],
                    'text-radial-offset': 0.5,
                    'text-justify': 'auto',
                    'icon-image': ['concat', ['get', 'icon'], '-15']
                }
            });



}
function set_marker (id, lng, lat) {

    markers[id] = new mapboxgl.Marker(
        {
        color: "#B917FC",
        scale:1.5,
        // sy
    }
    ).setPopup(popups[id])
        .setLngLat([lng, lat])
        .addTo(map);

}
const reverseGeocoding = function (longitude,latitude) {
    var url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/'
            + longitude + ',' + latitude
            + '.json&access_token=' + mapboxgl.accessToken;
    console.log(url)
    // var xmlHttp = new XMLHttpRequest();
    // xmlHttp.open( "GET", url, false ); // false for synchronous request
    // xmlHttp.send( null );

   return xmlHttp.responseText;
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
    var xy = '"'+coordinates.lng.toString()+','+coordinates.lat.toString()+'"'
    // console.log(reverseGeocoding(coordinates.lng.toString(),coordinates.lat.toString()))
    // document.getElementById("mapboxaddress").setAttribute('value',ee)

}


function flat_change_house(e) {
    // alert(e.target.value);
}

function add_sector_source(id, json, popup_data){
    sectors.push({
                'id': id,
                "type": "Feature",
                "properties":{
                    'name':popup_data,
                },
                "geometry": json,
            });
    popups[id] = new mapboxgl.Popup(
            {
                offset: 25,
                closeButton: false,
                closeOnClick: true,
            },
        ).setHTML(
            popup_data
    )
}

function map_add_layer(){
    // sources = {
    map.addSource(
            'layers', {
                'type': 'geojson',
                'data': {
                    'type': 'FeatureCollection',
                    'features': sectors,
                },
    })

        // )
    map. addLayer({
        'id': 'sectors',
        'type':'fill',
        'source': 'layers',
        'layout': {},
        'paint':{
            'fill-color': '#0080ff', // blue color fill
            'fill-opacity': 0.5
        }
    })
}

// function add_source() {
//     const sectors= JSON.parse(document.getElementById('sectors_data').textContent)
//     features = []
//     for (let id in sectors) {
//         features.push({
//                 "type": "Feature",
//                 "properties":{
//                     'id': id,
//                     'name':sectors[id]['name']
//                 },
//                 "geometry": JSON.parse(sectors[id]['geojson'])
//             });
//         popups[id] = new mapboxgl.Popup(
//             {
//                 offset: 25,
//                 closeButton: false,
//                 closeOnClick: true,
//             },
//         ).setHTML(
//             sectors[id]['name']
//         )
//     }
//     map.addSource(
//             'layers', {
//                 'type': 'geojson',
//                 'data': {
//                     'type': 'FeatureCollection',
//                     'features': features,
//                 },
//             },
//         )
// }
// function add_sectors(){
//     map. addLayer({
//         'id': 'sectors',
//         'type':'fill',
//         'source': 'layers',
//         'layout': {},
//         'paint':{
//             'fill-color': '#0080ff', // blue color fill
//             'fill-opacity': 0.5
//         }
//     })
// }

function sector_popup(e) {
    id = e.features[0].id
    popups[id].setLngLat(e.lngLat).addTo(map);
        // .setHTML(e.features.properties.id)
// .addTo(map);
}

function add_draw_control() {
    draw = new MapboxDraw({
        displayControlsDefault: false,
        // Select which mapbox-gl-draw control buttons to add to the map.
        controls: {
        polygon: true,
        trash: true
        },
        // Set mapbox-gl-draw to draw by default.
        // The user does not have to click the polygon control button first.
        defaultMode: 'draw_polygon'
        });

    map.addControl(draw);

}

function list2string(l){
    var result = []
    for (i in l){
        result.push(l[i].join(' '))
    }
    return '(('+result.join(',')+'))'
}

function update_sector(event) {
    const data = draw.getAll();
    var coordinates = draw.getAll()['features'][0]['geometry']['coordinates'][0]
    document.getElementById("contour").setAttribute(
        'value',"SRID=4326;POLYGON"+list2string(coordinates))
    // console.log(document.getElementById('contour').value)
}
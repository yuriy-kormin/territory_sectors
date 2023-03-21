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
// mapboxgl.setRTLTextPlugin('https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-rtl-text/v0.2.3/mapbox-gl-rtl-text.js');
// map.addControl(new MapboxLanguage({defaultLanguage: 'ru'}));
var markers = {};
var popups = {};
var sectors = [];

// var sector_sources = {};

function map_fly(point_x,point_y){
    map.flyTo({
        center: [point_x,point_y]
    })
}
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
function set_marker (id, lng, lat, color = 'default') {
    let color_val = serve_status_color;
    if (color !== 'default'){
        color_val = search_status_color
    }
    markers[id] = new mapboxgl.Marker(
        {
        color: color_val,
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

}
function add_sector_source(id, json,for_search,popup_data){
    sectors.push({
                'id': id,
                "type": "Feature",
                "properties":{
                    'name':popup_data,
                    'for_search':for_search
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
function map_add_layer(mark_id = false){

    map.addSource(
            'layers', {
                'type': 'geojson',
                'data': {
                    'type': 'FeatureCollection',
                    'features': sectors,
                },
    })

    map.addLayer({
        'id': 'sectors',
        'type':'fill',
        'source': 'layers',
        'layout': {},
        'paint':{
            'fill-color': serve_status_color,
            'fill-opacity': 0.5
        },
        'filter': ['==', 'for_search', false]
    })


    map.addLayer({
        'id': 'sectors-search',
        'type':'fill',
        'source': 'layers',
        'layout': {},
        'paint':{
            'fill-color': search_status_color,
            'fill-opacity': 0.5
        },
        'filter': ['==', 'for_search', true]
    })
}


function sector_popup(e) {
    id = e.features[0].id
    popups[id].setLngLat(e.lngLat).addTo(map);
}

function add_draw_control() {
    draw = new MapboxDraw({
        displayControlsDefault: false,
        controls: {
        polygon: true,
        trash: true
        },
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

function show_all_popups(){
    for (var key in markers ) {
        markers[key].getPopup().addTo(map);
    }
}
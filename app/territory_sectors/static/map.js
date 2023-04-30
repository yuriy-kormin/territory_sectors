const map = new mapboxgl.Map({
container: 'map', // container ID
style: 'mapbox://styles/yuriykormin/clgyzsbgn00gs01pg4gmabbng', // style URL
center: [41.612803, 41.632153], // starting position [lng, lat]
zoom: 16, // starting zoom
language: 'ru-RU'
});
map.addControl(new mapboxgl.FullscreenControl({container: document.querySelector('#map')}));
map.addControl(new mapboxgl.GeolocateControl({
    positionOptions: {
        enableHighAccuracy: true
    },
    trackUserLocation: true,
    showUserHeading: true
}));
// map.addControl(new mapboxgl.NavigationControl({showZoom:false}));
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
    ).setHTML(text)
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
    let color_val = search_status[false];
    if (color !== 'default'){
        color_val = search_status[true]
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
function add_sector_source(id,status,json,for_search,popup_data){
    sectors.push({
                'id': id,
                "type": "Feature",
                "properties":{
                    'name':status,
                    'for_search':for_search,
                    'status':status,
                    'id': id,
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
        'id': "outline_sector_search",
        'type':'line',
        'source': 'layers',
        'layout': {},
        'paint':{
            'line-color': search_status[true],
            'line-width': 2,
        },
        'filter': ['==', 'for_search', true]
    })

    map.addLayer({
        'id': "outline_sector_ready",
        'type':'line',
        'source': 'layers',
        'layout': {},
        'paint':{
            'line-color': search_status[false],
            'line-width': 2,
        },
        'filter': ['==', 'for_search', false]
    })

    for (status_name in sector_status){
        map.addLayer({
        'id': 'sector_'+status_name,
        'type': 'fill',
        'source': 'layers',
        'layout': {},
        'paint': {
            'fill-color': sector_status[status_name],
            'fill-opacity': 0.5
            // 'line-color': sector_status[status_name],
            // 'line-width': 4
        },
        'filter': ['==', 'status', status_name]
        })
    }

}


function sector_popup(e) {
    id = e.features[0].properties.id
    popups[id].setLngLat(e.lngLat).addTo(map);
    // console.log(map.getStyle().layers)

}

function handleClickEvent(e) {
     // var features = map.queryRenderedFeatures(e.point);

      // var layerList = features.map(function(feature) {
      //   return feature.layer.id;
      // });

    //
    let sectors_layers_names = [
        'sector_free',
        'sector_assigned',
        'sector_completed',
        'sector_under_construction'
    ]
    let houses_layers_names = [
        'circle-houses-layer',
        'circle-houses-search-layer'
    ]

    var layerList = map.queryRenderedFeatures(e.point, { layers: sectors_layers_names.concat(houses_layers_names) });
    house_layer = layerList.filter(function(value) {
                                   return houses_layers_names.indexOf(value.layer.id) > -1;
                               });
    sector_layer = layerList.filter(function(value) {
                                   return sectors_layers_names.indexOf(value.layer.id) > -1;
                               });
    if (house_layer.length){
        id = house_layer[0].properties.id;
        popups[id].setLngLat(e.lngLat).addTo(map);
    } else {
        if (sector_layer.length){
            id = sector_layer[0].properties.id;
            popups[id].setLngLat(e.lngLat).addTo(map);
        }
    }


    // if (is_house) {
    //     // console.log(e)
    //     var features = map.queryRenderedFeatures(e.podFeatures(e.point, { layers: sectors_layers_names }));
    //     // if (is_sector){
    //     //     // id = features[0].properties.id
    //     //     // popups[id].setLngLat(e.lngLat).addTo(map);
    //     // }
    // }int, { layers: houses_layers_names });
    //     id = features[0].properties.id
    //     popups[id].setLngLat(e.lngLat).addTo(map);
    // } else {
    //     var features = map.queryRendere

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
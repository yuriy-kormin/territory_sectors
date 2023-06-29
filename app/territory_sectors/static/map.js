const map = new mapboxgl.Map({
container: 'map', // container ID
style: 'mapbox://styles/mapbox/streets-v12?optimize=true',
// style: 'mapbox://styles/yuriykormin/clgyzsbgn00gs01pg4gmabbng?optimize=true', // style URL
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
// var popups = {};
var sectors = [];

// var sector_sources = {};

function map_fly(point_x,point_y){
    map.flyTo({
        center: [point_x,point_y]
    })
}
// function set_popup (id, text) {
//     popups[id] = new mapboxgl.Popup(
//         {
//             offset: 25,
//             closeButton: false,
//             closeOnClick: true,
//         },
//     ).setHTML(text)
// }

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
function set_marker (id, lng, lat, color = 'default', text_data='') {
    let color_val = search_status[false];
    if (color !== 'default'){
        color_val = search_status[true]
    }
    const popup = new mapboxgl.Popup(
        {
            offset: 25,
            closeButton: false,
            closeOnClick: true,
        },
    ).setHTML(text_data)

    markers[id] = new mapboxgl.Marker(
        {
        color: color_val,
        scale:1.5,
        // sy
    }).setPopup(popup)
    .setLngLat([lng, lat])
    .addTo(map);

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
            })
    // popups[id] = new mapboxgl.Popup(
    //         {
    //             offset: 25,
    //             closeButton: false,
    //             closeOnClick: true,
    //         },
    //     ).setHTML(
    //         popup_data
    // )
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
    //     map.addLayer({
    //     'id': "outline_sector_search",
    //     'type':'line',
    //     'source': 'layers',
    //     'layout': {},
    //     'paint':{
    //         'line-color': search_status[true],
    //         'line-width': 2,
    //     },
    //     'filter': ['==', 'for_search', true]
    // })

    // map.addLayer({
    //     'id': "outline_sector_ready",
    //     'type':'line',
    //     'source': 'layers',
    //     'layout': {},
    //     'paint':{
    //         'line-color': search_status[false],
    //         'line-width': 2,
    //     },
    //     'filter': ['==', 'for_search', false]
    // })

    map.addLayer({
        'id': 'sectors',
        'type': 'fill',
        'source': 'layers',
        'layout': {},
        'paint': {
            'fill-color': ['get', 'color'],
            'fill-opacity': 0.6
        },
        })

}


// function sector_popup(e) {
//     id = e.features[0].properties.id
//     popups[id].setLngLat(e.lngLat).addTo(map);
// }

const loading_spinner = `
        <div className="spinner-border text-primary" role="status">
            <span className="sr-only">Loading...</span>
        </div>
        `
function handleClickEvent(e) {
    const sectors_layers_name = 'sectors'
    const houses_layers_names = 'circle-houses'

    var layerList = map.queryRenderedFeatures(e.point) //, { layers: [sectors_layers_name,houses_layers_names] });
    // console.log('layers',typeof layerList)
    let type = "";
    if (layerList.length > 0) {
        layerList.forEach(layer=> {
            if (layer.layer.id === houses_layers_names){
                type = 'house';
                id = layer.properties.id;
            } else if (layer.layer.id === sectors_layers_name){
                type = 'sector';
                id = layer.properties.id;
            }
        })
  }
    if (type !== '' && id !== -1) {
        const popup = new mapboxgl.Popup(
            {
                closeOnClick: true,
                offset: 25,
                closeButton: false,
            }
        ).setLngLat(e.lngLat)
            .setHTML(loading_spinner)
            .addTo(map);
        getPopupHTML(type, id)
            .then(result =>{
                popup.setHTML(result)
                })

    }
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
}

function show_all_popups(){
    for (var key in markers ) {
        markers[key].getPopup().addTo(map);
    }
}
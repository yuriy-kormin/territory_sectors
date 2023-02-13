function create_uuid(){
    fetch('/uuid/gen')
}
let circles = []
function add_circle_source(id, msg, lng, lat){
    circles.push({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [lng, lat]
        },
        "properties": {
            "title": msg,
        }
    })

//     circles[id] = new mapboxgl.so(
//         {
//         // color: "#B917FC",
//         scale:1.5,
//         // sy
//     }
//     ).setLngLat([lng, lat])
//         .addTo(map);
}

function add_map_circles_source(){
     map.addSource("circles", {
         "type": "geojson",
         "data": {
             "type": "FeatureCollection",
             "features": circles
         }
     })


    // console.log("its a circles", circles)

}


function add_circles_layer(){
    map.addLayer({
    'id': 'houses-layer',
    'type': 'circle',
    'source': 'circles',
    'paint':{
        'circle-radius': 16,
        'circle-stroke-width': 2,
        'circle-color': 'red',
        'circle-stroke-color': 'white'
    }
});
}
function add_symbols_layer(){
    map.addLayer({
    'id': 'houses-msg-layer',
    'type': 'symbol',
    'source': 'circles',
    layout: {
        'text-field': "{title}",
        'text-font': ['DIN Offc Pro Medium', 'Arial Unicode MS Bold'],
        'text-size': 20
    },
    paint: {
            'text-color': '#4FA627',
        }
});
}
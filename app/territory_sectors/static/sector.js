function create_uuid(){
    fetch('/uuid/gen')
}
let circles = []
function add_circle_source(id, msg, mark ="default",lng, lat){
    circles.push({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [lng, lat],

        },
        "properties": {
            "title": msg,
            "mark":mark,
            "id":`house_${id}`,
        },
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
}


function add_circles_layer(){
    map.addLayer({
    'id': 'circle-houses-layer',
    'type': 'circle',
    'source': 'circles',
    'paint':{
        'circle-radius': 16,
        'circle-stroke-width': 2,
        'circle-color': search_status[false],
        'circle-stroke-color': 'white'
    },
    'filter': ['==', 'mark', 'default']
});
    map.addLayer({
    'id': 'circle-houses-search-layer',
    'type': 'circle',
    'source': 'circles',
    'paint':{
        'circle-radius': 16,
        'circle-stroke-width': 2,
        'circle-color': search_status[true],
        'circle-stroke-color': 'white'
    },
    'filter': ['!=', 'mark', 'default']
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
            'text-color': '#383a37',
        }
});
}
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function encodeFormData(data) {
  var encodedData = '';
  for (var prop in data) {
    if (data.hasOwnProperty(prop)) {
      if (encodedData.length > 0) {
        encodedData += '&';
      }
      encodedData += encodeURIComponent(prop) + '=' + encodeURIComponent(data[prop]);
    }
  }
  return encodedData;
}

function checkinout(markerId, action) {
  var csrfToken = getCookie('csrftoken');

  const data_to_send = {
      action: action,
  }
  var xhr = new XMLHttpRequest();
  xhr.open('POST', `/sector/${markerId}/checkinout/`);
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.setRequestHeader('X-CSRFToken', csrfToken);
  xhr.withCredentials = true;  // Add this line to enable authentication credentials
  xhr.send(JSON.stringify(data_to_send))
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // Show a success message if the request is successful
      var response = JSON.parse(xhr.responseText);
      alert(response.message);
    }
  };
  xhr.send(encodeFormData(markerId));
}

$(function() {
    function showModal(imageUrl) {
    var image = $('<img>').attr('src', imageUrl);
    image.id = "modal-image"
        image.addClass("img-fluid")
    $('#imagemodal .modal-body').html(image);
    $('#imagemodal').modal('show');
  }

  $('.pop').on('click', function(event) {
    // var imageUrl = url;
    // var image = $('<img>').attr('src', imageUrl);
    // $('#imagemodal .modal-body').html(image);
    // $('#imagemodal').modal('show');
    event.preventDefault();
    var fullImageUrl = $(this).data('url');
    showModal(fullImageUrl);
  });
});



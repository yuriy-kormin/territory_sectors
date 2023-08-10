import Map, { NavigationControl, GeolocateControl } from 'react-map-gl';
import "./hideLogo.css";

const DivMap = () => {
    const MAPBOX_TOKEN = 'pk.eyJ1IjoieXVyaXlrb3JtaW4iLCJhIjoiY2xjdTZjMm1jMHJwZTNvbXg1cm1xMGh5ciJ9.uHPoJEdjly2KUEmc8YEOkw';
    return (
        <Map
            mapboxAccessToken={MAPBOX_TOKEN}
            initialViewState={{
                longitude: 41.612803,
                latitude: 41.632153,
                zoom: 15
            }}
            style={{width: "100vw", height: "100vh"}}
            mapStyle="mapbox://styles/mapbox/streets-v12?optimize=true"
            dragRotate={false}
            touchZoomRotate={false}>
            <NavigationControl />
            <GeolocateControl />
        </Map>
    )
};

export default DivMap;
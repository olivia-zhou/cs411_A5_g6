import React from "react";
import {GoogleMap, useLoadScript} from "@react-google-maps/api";

const libraries = ["places"];
const mapContainerStyle = {
    height: "50vh",
    width: "80vw"
};

const center = {
    lat: 42.3497644,
    lng: -71.1041491
};

function Map() {
    const {isLoaded, loadError} = useLoadScript({
        googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAPS_API_KEY,
        libraries
    });

    if (loadError) return "Error";
    if (!isLoaded) return "Loading...";

    return (
        <div>
            <br/>
            <p>Search your destination</p>
            <GoogleMap
                id="map"
                mapContainerStyle={mapContainerStyle}
                zoom={8}
                center={center}
            >
            </GoogleMap>
        </div>
    );
}

export default React.memo(Map);


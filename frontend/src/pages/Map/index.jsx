import React from 'react';
import {
  MapContainer,
  TileLayer,
} from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

const Map =()=>{
  return ( 
  <>
  <center>
      <MapContainer
        center={[3.450541, -76.534630]}
        zoom={12}
        scrollWheelZoom={false}
        style={{ width: '90vw', height: '60vh', borderRadius:3, borderColor :'red' }}
      >
        <TileLayer
          attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
      </MapContainer>
      <h6>Workouts</h6>
      </center>
    </>
  )
}

export default Map;
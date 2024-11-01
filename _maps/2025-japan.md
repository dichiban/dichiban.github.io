---
layout: map
title: 2025 Japan
---

<div style="text-align: justify" markdown="1">
<div id="map"></div>

<script>

var map = L.map('map').setView([35.652, 139.839], 7);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var Esri_WorldStreetMap = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
	attribution: '2012'
});

Esri_WorldStreetMap.addTo(map);
var accomodation = {{ site.data.locations.2025-japan.accomodation.features | sort: 'properties.startDate' | jsonify }}
var activity     = {{ site.data.locations.2025-japan.activity.features     | sort: 'properties.startDate' | jsonify }}

const pathCoords = [];
accomodation.forEach(location => {
     var coord = location.geometry.coordinates;
     pathCoords.push([coord[0], coord[1]]);
});

const accCoords = [];
activity.forEach(location => {
     var d = location.properties.startDate;
     accomodation.forEach(acc => {
          if (d >= acc.properties.startDate && d < acc.properties.endDate) {

               var c1 = location.geometry.coordinates;
               var c2 = acc.geometry.coordinates;
               accCoords.push([[c2[0], c2[1]], [c1[0], c1[1]]]);
          }
     });
});

accCoords.forEach(line => {
     L.polyline(line, {
          color: 'black',
          weight: 5,   // Thicker than the main polyline
          opacity: 1}
          ).addTo(map);
     L.polyline(line, {color: "#cde43b"}).addTo(map);

})
var accomMarkerOptions = {
    radius: 10,
    fillColor: "#ff7800",
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
};

var activityMarkerOptions = {
    radius: 10,
    fillColor: "#cde43b",
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
};

var outline = L.polyline(pathCoords, {
    color: 'black',
    weight: 5,   // Thicker than the main polyline
    opacity: 1
}).addTo(map);

var pathLine = L.polyline(pathCoords, {color: "#ff7800"}).addTo(map);

const accomMarkers = {};
const activityMarkers = {};

</script>

<br>

{% assign data1 = site.data.locations.2025-japan.accomodation.features %}
{% assign data2 = site.data.locations.2025-japan.activity.features %}
{% assign combined_data = data1 | concat: data2 %}
{% assign sorted_data = combined_data | sort: "properties.startDate" %}
{% for feature in sorted_data %}
{% if "accomodation" == feature.properties.type %}

<details class="accom-collapse" collapse-id="{{ feature.properties.name }}">
  <summary class="accom-summary"><b>{{ feature.properties.name }}</b><div class="right">{{ feature.properties.startDate | date: "%d %B, %Y" }} - {{ feature.properties.endDate | date: "%d %B, %Y" }}</div></summary>
  <div class="accom-item" data-id="{{ feature.properties.name }}">
  <div><b>Address</b> : <a href="{{ feature.properties.link }}">{{ feature.properties.address }}</a></div>
  <div><b>Check-in</b> : {{ feature.properties.checkIn }}</div>
  <div><b>Check-out</b> : {{ feature.properties.checkOut }}</div>
  <div><b>Cost</b> : {{ feature.properties.cost }} {{ feature.properties.currency }}</div>
  <div><b>Notes</b> : {{ feature.properties.notes }}</div>
  </div>
</details>
{% elsif "activity" == feature.properties.type %}
<details class="activity-collapse" collapse-id="{{ feature.properties.name }}">
  <summary class="activity-summary"><b>{{ feature.properties.name }}</b><div class="right">{{ feature.properties.startDate | date: "%d %B, %Y" }}</div></summary>
  <div class="activity-item" data-id="{{ feature.properties.name }}">
  <div><b>Address</b> : <a href="{{ feature.properties.link }}">{{ feature.properties.address }}</a></div>
  <div><b>Description</b> : {{ feature.properties.description }}</div>
  {% if feature.properties.cost %}
  <div><b>Price</b> : {{ feature.properties.cost }} {{ feature.properties.currency }}</div>
  {% endif %}
  </div>
</details>
{% endif %}
{% endfor %}

<script>
// Function to reset all markers to their default style
function resetAccomMarkerStyles() {
  Object.values(accomMarkers).forEach(marker => {
    marker.setStyle(accomMarkerOptions);
  });
}

// Function to reset all HTML elements to default style
function resetAccomLocationStyles() {
  document.querySelectorAll('.accom-collapse').forEach(item => {
    item.style.border = '';  // Reset background color
  });
}

// Function to reset all markers to their default style
function resetActivityMarkerStyles() {
  Object.values(activityMarkers).forEach(marker => {
    marker.setStyle(activityMarkerOptions);
  });
}

// Function to reset all HTML elements to default style
function resetActivityLocationStyles() {
  document.querySelectorAll('.activity-collapse').forEach(item => {
    item.style.border = '';  // Reset background color
  });
}

function resetMarkersStyles() {
  resetAccomMarkerStyles();
  resetActivityMarkerStyles();
}

function resetLocationStyles() {
     resetAccomLocationStyles();
     resetActivityLocationStyles();
}

// Function to highlight a specific marker and its HTML element
function highlightLocation(marker, itemId) {
  // Highlight the marker
  marker.setStyle({
    color: 'red',
    fillColor: '#f30',
    radius: 12,
  });

  // Highlight the corresponding HTML element
  var borderStyle = "3px solid red";
  var item = document.querySelector(`.accom-collapse[collapse-id="${itemId}"]`);
  if (item) {
    item.style.border = borderStyle;
    item.setAttribute('open',true);
  }

  item = document.querySelector(`.activity-collapse[collapse-id="${itemId}"]`);
  if (item) {
    item.style.border = borderStyle;
    item.setAttribute('open',true);
  }
}

accomodation.forEach(location => {
     var coord = location.geometry.coordinates;
     const marker = L.circleMarker([coord[0], coord[1]], 
     accomMarkerOptions).addTo(map)
     accomMarkers[location.properties.name] = marker
       // Add a click event listener to the marker
     marker.bindPopup(location.properties.name);
     marker.on('click', () => {
          // Reset all markers and location styles
          resetMarkersStyles();
          resetLocationStyles();
          // Highlight the clicked marker and corresponding location div
          highlightLocation(marker, location.properties.name);
     });
});

activity.forEach(location => {
  var coord = location.geometry.coordinates;
  const marker = L.circleMarker([coord[0], coord[1]], 
  activityMarkerOptions).addTo(map)
  activityMarkers[location.properties.name] = marker
    // Add a click event listener to the marker
  marker.bindPopup(location.properties.name);
  marker.on('click', () => {
    // Reset all markers and location styles
    resetMarkersStyles();
    resetLocationStyles();
    // Highlight the clicked marker and corresponding location div
    highlightLocation(marker, location.properties.name);
  });
});

// Add click event listener to each HTML element
document.querySelectorAll('.accom-item').forEach(item => {
  item.addEventListener('click', () => {
    // Get the marker ID from the data attribute
    const markerId = item.getAttribute('data-id');
    // Reset all markers to their original style
    resetMarkersStyles();
    resetLocationStyles();

    // Highlight the selected marker
    const selectedMarker = accomMarkers[markerId];
    if (selectedMarker) {
      highlightLocation(selectedMarker, markerId);
      
      // Optionally, pan and zoom to the marker
      // map.setView(selectedMarker.getLatLng(), 15);
    }
  });
});

// Add click event listener to each HTML element
document.querySelectorAll('.activity-item').forEach(item => {
  item.addEventListener('click', () => {
    // Get the marker ID from the data attribute
    const markerId = item.getAttribute('data-id');
    // Reset all markers to their original style
    resetMarkersStyles();
    resetLocationStyles();

    // Highlight the selected marker
    const selectedMarker = activityMarkers[markerId];
    if (selectedMarker) {
      highlightLocation(selectedMarker, markerId);
      
      // Optionally, pan and zoom to the marker
      // map.setView(selectedMarker.getLatLng(), 15);
    }
  });
});

</script>
</div>

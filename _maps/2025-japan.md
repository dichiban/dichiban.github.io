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
     var d = location.properties.date;
     accomodation.forEach(acc => {
          if (d >= acc.properties.startDate && d < acc.properties.endDate) {

var c1 = location.geometry.coordinates;
               var c2 = acc.geometry.coordinates;
               accCoords.push([[c2[0], c2[1]], [c1[0], c1[1]]]);
          }
     });
});

accCoords.forEach(line => {
     L.polyline(line, {color: "#6495ED"}).addTo(map);
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
    fillColor: "#6495ED",
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
};

var pathLine = L.polyline(pathCoords, {color: "#ff7800"}).addTo(map);

const accomMarkers = {};
const activityMarkers = {};

</script>

<!-- <details>
  <summary>Click me</summary>
  
  ### Heading
  1. Foo
  2. Bar
     * Baz
     * Qux

</details> -->

<!-- {{ site.data.locs | inspect }}
{{ site.data.locations.2025-japan.accomodation | inspect }} -->

hello
{% assign data1 = site.data.locations.2025-japan.accomodation.features %}
{% assign data2 = site.data.locations.2025-japan.activity.features %}
{% assign combined_data = data1 | concat: data2 %}
{% assign sorted_data = combined_data | sort: "properties.startDate" %}
{% for feature in sorted_data %}
{% if "accomodation" == feature.properties.type %}
<details class="accom-collapse" collapse-id="{{ feature.properties.name }}">
  <summary class="accom-summary">{{ feature.properties.name }}<div class="right">{{ feature.properties.startDate | date: "%d %B, %Y" }} - {{ feature.properties.endDate | date: "%d %B, %Y" }}</div></summary>
  <div class="accom-item" data-id="{{ feature.properties.name }}">
  <div>Address : {{ feature.properties.address }}</div>
  <div>Check-in : {{ feature.properties.checkIn }}</div>
  <div>Check-out : {{ feature.properties.checkOut }}</div>
  </div>
</details>
{% elsif "activity" == feature.properties.type %}
<details class="activity-collapse" collapse-id="{{ feature.properties.name }}">
  <summary class="activity-summary">{{ feature.properties.name }}<div class="right">{{ feature.properties.startDate | date: "%d %B, %Y" }}</div></summary>
  <div class="activity-item" data-id="{{ feature.properties.name }}">Address : {{ feature.properties.address }}</div>
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
  document.querySelectorAll('.accom-item').forEach(item => {
    item.style.backgroundColor = '';  // Reset background color
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
  document.querySelectorAll('.activity-item').forEach(item => {
    item.style.backgroundColor = '';  // Reset background color
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
  var item = document.querySelector(`.accom-collapse[collapse-id="${itemId}"]`);
  if (item) {
     var elem = document.querySelector(`.accom-item[data-id="${itemId}"]`);
     elem.style.background = "#fd851b";
     item.setAttribute('open',true);
  }

  item = document.querySelector(`.activity-collapse[collapse-id="${itemId}"]`);
  if (item) {
     var elem = document.querySelector(`.activity-item[data-id="${itemId}"]`);
     elem.style.background = "#3479fa";
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

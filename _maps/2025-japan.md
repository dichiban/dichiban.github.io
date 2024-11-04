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
var accomodations = {{ site.data.locations.2025-japan.accomodation.features | sort: 'properties.startDate' | jsonify }}
var activities     = {{ site.data.locations.2025-japan.activity.features     | sort: 'properties.startDate' | jsonify }}

t1_hotel = "Le Petit Tokyo";
apa_hotel = "APA Hotel Karuizawa Ekimae Karuizawaso";
kanemidori = "Kanemidori";
matsumoto = "Airbnb Home in Matsumoto";

var journey = [t1_hotel, "Lake Kawaguchiko", t1_hotel,
               apa_hotel, "Hiroshi Senju Museum Karuizawa", apa_hotel,
               "Karuizawa Prince Shopping Plaza", apa_hotel,
               "Usui Pass", "Shiraito Falls", "Harunire Terrace", apa_hotel,
               kanemidori, "Sainokawara Park", "Seirakuen Fishing", kanemidori,
               "Jigokudani Yaen Koen", "Matsumoto Castle", matsumoto,
               "Narai Juku", "Khang's House"];

var accomMap = {};

for (let i = 0; i < accomodations.length; i++)
{
  accomMap[accomodations[i].properties.name] = accomodations[i];
}

var activityMap = {};

for (let i = 0; i < activities.length; i++)
{
  activityMap[activities[i].properties.name] = activities[i];
}

const activityCoords = [];
const accomCoords = []

const activityToAccom = [];
const accomToActivity = [];

for (let i = 1; i < journey.length-1; i++) {
  const j1 = journey[i-1];
  const j2 = journey[i];
  const j3 = journey[i+1];

  if (j1 == j3)
  {
    console.log(j1);
  }
}

const allPaths = []
var prevType = "accomodation";
var prevCoords = null;
journey.forEach(place => {
  var details = null
  var value = 0;
  var value2 = 1;
  if (place in activityMap) {
    details = activityMap[place];
  }

  if (place in accomMap) {
    details = accomMap[place];
    value = 1;
    value2 = 0;
  }

  var coords = details.geometry.coordinates;
  if (prevCoords === null) {
    prevCoords = coords;
    return;
  }

  var type = details.properties.type;
  if (prevType != type)
  {
    prevType = type;
    allPaths.push([
      [prevCoords[0], prevCoords[1], value], 
      [coords[0],     coords[1],     value2]
    ]);
  } else {
    allPaths.push([
      [prevCoords[0], prevCoords[1], value2], 
      [coords[0],     coords[1],     value2]
    ]);  
  }

  prevCoords = coords;
});


allPaths.forEach(line => {
  L.hotline(line, {
    min: 0,
    max: 1,
    palette: {
      0.0: '#ff7800', // orange
      1.0: '#cde43b'  // green
    },
    weight: 5,
    outlineColor: '#000000',
    outlineWidth: 1
  }).addTo(map);
})

var accomMarkerOptions = {
    radius: 10,
    fillColor: "#ff7800",
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 1
};

var activityMarkerOptions = {
    radius: 10,
    fillColor: "#cde43b",
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 1
};


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
  <div><b>Address</b> : <a href="{{ feature.properties.link }}" target="_blank">{{ feature.properties.address }}</a></div>
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
  <div><b>Address</b> : <a href="{{ feature.properties.link }}" target="_blank">{{ feature.properties.address }}</a></div>
  <div><b>Description</b> : {{ feature.properties.description }}</div>
  {% if feature.properties.cost %}
  <div><b>Price</b> : {{ feature.properties.cost }} {{ feature.properties.currency }}</div>
  {% endif %}
  {% if feature.properties.open %}
  <div><b>Open</b> : {{ feature.properties.open }}</div>
  {% endif %}
  {% if feature.properties.close %}
  <div><b>Close</b> : {{ feature.properties.close }}</div>
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

const popupOptions = {
  className: 'clickable-popup'  // Add the custom class to this popup
};

accomodations.forEach(location => {
  var coord = location.geometry.coordinates;
  const marker = L.circleMarker([coord[0], coord[1]], 
  accomMarkerOptions).addTo(map)
  accomMarkers[location.properties.name] = marker
    // Add a click event listener to the marker
  var name = location.properties.name;
  marker.bindPopup(name, popupOptions);
  marker.on('click', () => {
    // Reset all markers and location styles
    resetMarkersStyles();
    resetLocationStyles();
    // Highlight the clicked marker and corresponding location div
    highlightLocation(marker, name);
  });
});

activities.forEach(location => {
  var coord = location.geometry.coordinates;
  const marker = L.circleMarker([coord[0], coord[1]], 
  activityMarkerOptions).addTo(map)
  activityMarkers[location.properties.name] = marker
    // Add a click event listener to the marker
  var name = location.properties.name;
  marker.bindPopup(name, popupOptions);
  marker.on('click', () => {
    // Reset all markers and location styles
    resetMarkersStyles();
    resetLocationStyles();
    // Highlight the clicked marker and corresponding location div
    highlightLocation(marker, name);
  });
});


map.on("popupopen", function (e) {
    const popupElement = e.popup.getElement().querySelector('.leaflet-popup-content');
    popupElement.addEventListener("click", function () {
      console.log(e.popup.getContent());
      var targetId = e.popup.getContent();
      var summaryElement = document.querySelector(`.activity-collapse[collapse-id="${targetId}"]`);
      // Scroll to the summary element
      if (summaryElement) {
          summaryElement.scrollIntoView({ behavior: "smooth" });
          return;
      } 
  
      summaryElement = document.querySelector(`.accom-collapse[collapse-id="${targetId}"]`);
      if (summaryElement) {
          summaryElement.scrollIntoView({ behavior: "smooth" });
          return;
      }
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
      map.setView(selectedMarker.getLatLng());
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
      map.setView(selectedMarker.getLatLng());
    }
  });
});

</script>
</div>

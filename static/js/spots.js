  var collection = {{ content|geojsonfeature:"popupContent"|safe }};

  function onEachFeature(feature, layer) {
    if (feature.properties && feature.properties.popupContent) {
      layer.bindPopup(feature.properties.popupContent);
    }
  }

  function map_init(map, options) {
    L.geoJson(collection, {onEachFeature: onEachFeature}).addTo(map);
  }

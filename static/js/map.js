<script type="text/javascript">
	var collection = {{ rsquery|geojsonfeature|safe }};
	function map_init(map, options) {
		L.geoJson(collection).addTo(map);
	}
</script>
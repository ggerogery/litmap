from django.contrib import admin

# Register your models here.
from models import MapObjects
from leaflet.admin import LeafletGeoAdmin

class WeatherStationAdminAdmin(LeafletGeoAdmin):
    settings_overrides = {
       'DEFAULT_CENTER': (59.9505, 30.3167),
       'DEFAULT_ZOOM': 13,

    }

admin.site.register(MapObjects, WeatherStationAdminAdmin)
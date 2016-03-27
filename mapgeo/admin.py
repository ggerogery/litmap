from django.contrib import admin

# Register your models here.
from models import MapObjects
from leaflet.admin import LeafletGeoAdmin

admin.site.register(MapObjects, LeafletGeoAdmin)
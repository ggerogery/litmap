from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from mapgeo.models import MapObjects
from django.db import models
from djgeojson.fields import PointField

def pointmap(request):
	rsquery = MapObjects.objects.all()
	return render(request, 'mapgeo/pointmap.html', {'rsquery': rsquery})

#def pointcontent(request):
#	content = MapObjects.objects.all()
#	return render(request, 'mapgeo/base.html', {'content': content})

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from mapgeo.models import MapObjects

def pointmap(request):
	rsquery = MapObjects.objects.all()
	return render(request, 'mapgeo/pointmap.html', {'rsquery': rsquery})

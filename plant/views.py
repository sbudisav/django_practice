from django.shortcuts import render
from .models import Plant
from dnajgo.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def plant_list(request):
  plants = Plant.objects
  return render(request, 'plant/plant_list.html', {'plants': plants})
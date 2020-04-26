from django.shortcuts import render
from .models import Plant
from dnajgo.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def plant_list(request):
  plants = Plant.objects
  return render(request, 'plant/plant_list.html', {'plants': plants})

def plant_details(request, pk):
  plant = get_object_or_404(Plant, pk=pk)
  # NOTE: PK is a built in function, but is the variable as well? Could we use pk = plant_id? or just id? Is ID a built in funtion? 
  return render(request, 'plant/plant_detail.html', {'plant': plant})

# Note: no need for new or edit, as that will be handled from admin page.
# If we are to build a schedule do we do it here or do we do it from a scheduling app? 

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    form = UserCreationForm
    return render(request = request,
                  template_name = "templates/register.html",
                  context={"form":form})
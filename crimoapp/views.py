# views.py
from django.shortcuts import render
from .models import Disaster

def home(request):
    disasters = Disaster.objects.all()  # Fetch all disaster data
    return render(request, 'crimohtml.html', {'disasters': disasters})

def resources(request):
    disasters = Disaster.objects.all()  # Fetch all disaster data
    return render(request, 'resources.html', {'disasters': disasters})

def dashboard(request):
    disasters = Disaster.objects.all()
    return render(request, 'dashboard.html', {'disasters': disasters})

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import EmergencyAlert  



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

@csrf_exempt
def alertsend(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            lat = data.get("lat")
            lon = data.get("lon")

            EmergencyAlert.objects.create(latitude=lat, longitude=lon)
            return JsonResponse({"status": "received", "lat": lat, "lon": lon})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)
# views.py
from django.shortcuts import render
from .models import Disaster
import json
import os
from .utils import send_notification


def report(request):
    if request.method == "POST":
        report = {
            "name": request.POST["name"],
            "id": request.POST["id"],
            "location": request.POST["location"],
            "description": request.POST["description"],
            "time": request.POST["time"]
        }

        file_path = "campus_safe_reports.json"

        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, "r") as file:
                reports = json.load(file)
        else:
            reports = []
        
        reports.append(report)

        with open(file_path, "w") as file:
            json.dump(reports, file, indent=2)
    
        send_notification(
            info=report['description'],
            location=f"At: {report['location']}"
        )

    return render(request, "report.html")

        

def home(request):
    disasters = Disaster.objects.all()  # Fetch all disaster data
    return render(request, 'crimohtml.html', {'disasters': disasters})

def resources(request):
    disasters = Disaster.objects.all()  # Fetch all disaster data
    return render(request, 'resources.html', {'disasters': disasters})

def dashboard(request):
    file_path = "campus_safe_reports.json"

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r") as file:
            disasters = json.load(file)
    else:
        disasters = []

    return render(request, 'dashboard.html', {'disasters': disasters})

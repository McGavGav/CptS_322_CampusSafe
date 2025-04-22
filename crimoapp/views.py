# views.py
from django.shortcuts import render, redirect
from .models import Disaster
import json
import os
from .utils import send_notification
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User  # Ensure this is imported
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


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

def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            messages.success(request, "User registered successfully!")
            return redirect('registration_success')  # Redirect to success page
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration.html', {'form': form})

def registration_success(request):
    return render(request, 'registrationSuccess.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  # Redirect to the home page immediately
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')  # Re-render the login page with an error message
    return render(request, 'login.html')  # Render the login page for GET requests

@login_required
def view_report_history(request):
    file_path = "campus_safe_reports.json"

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r") as file:
            reports = json.load(file)
    else:
        reports = []

    # Filter reports by the logged-in user's ID
    user_reports = [report for report in reports if report["id"] == str(request.user.id)]

    return render(request, 'report_history.html', {'reports': user_reports})


def logout_user(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
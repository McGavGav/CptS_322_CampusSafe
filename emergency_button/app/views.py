from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import EmergencyAlert
import json


# Create your views here.
def showButton(request):
    return render(request, 'alertButton.html', { 'name': ''})

def home(request):
    return render(request, 'home.html', {'alert_button_url': '/app/alert/'})

@csrf_exempt 

#received locations
# def locRec(request):
#     if request.method == 'POST': 
#         lat = request.POST.get('latitude')
#         lon = request.POST.get('longitude')  # Typo here: should be 'longitude'
#         return JsonResponse({'status': 'success'})
#     return JsonResponse({'status': 'failed'}, status=400)


def trigger_emergency(request):
    if request.method == 'POST':
        data = request.POST
        lat = data.get('latitude')
        lon = data.get('longitude')
        EmergencyAlert.objects.create(
            user=request.user if request.user.is_authenticated else None,
            status='active',
            latitude=lat,
            longitude=lon
        )
        return JsonResponse({'status': 'success', 'message': 'Help is on the way!'})
    return JsonResponse({'status': 'fail'})


def cancel_emergency(request):
    if request.method == 'POST':
        EmergencyAlert.objects.filter(status='active').update(status='cancelled')
        return JsonResponse({'status': 'cancelled'})
    return JsonResponse({'status': 'fail'})


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully!")
            return redirect('registration_success')  # Redirect to the success page
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        form = UserCreationForm()
    
    return render(request, 'registerUser.html', {'form': form})

def registration_success(request):
    return render(request, 'registrationSuccess.html')

from django.contrib.auth import authenticate, login

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
    return redirect('register_user')  # Redirect back to the registration page

def report_incident(request):
    return render(request, 'reportIncident.html')

def report_history(request):
    return render(request, 'reportHistory.html')
def safety_resources(request):
    return render(request, 'safetyResources.html')

def maps(request):
    return render(request, 'maps.html')


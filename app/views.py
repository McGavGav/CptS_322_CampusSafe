from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
import json


# Create your views here.
def showButton(request):
    return render(request, 'alertButton.html', { 'name': ''})

def home(request):
    return render(request, 'home.html')

@csrf_exempt 
#received locations
def locRec(request):
    if request.method == 'POST': 
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')  # Typo here: should be 'longitude'
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully!")
            return redirect('registration_success')
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        form = UserCreationForm()
    
    return render(request, 'registerUser.html', {'form': form})
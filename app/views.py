from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from .forms import UserRegistrationForm
import json


# Create your views here.
def showButton(request):
    return render(request, 'alertButton.html', { 'name': ''})

@csrf_exempt 
#received locations
def locRec(request):
    if request.method == 'POST' : 
        lat = request.POST.get('latitude')
        lon = request.POST.get('logitude')
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed' }, status = 400 )

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
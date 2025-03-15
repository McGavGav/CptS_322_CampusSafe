from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 
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
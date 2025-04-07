from django.shortcuts import render
from .models import Incident
import json


def incidentMap (request):
  incident = Incident.objest.all()
  incident_json = json.dumps ([{'name' : i.name,
                                'description' : i.description,
                                'latitude' : i.latitude, 
                                'longitude' : i.longitude}
                                for i in incident])
  return render (request, 'incidentMap.html', {'incident_json':incident_json})
  

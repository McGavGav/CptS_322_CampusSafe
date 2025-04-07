from django.urls import path
from .views import IncidentMap

url = [ path('incident-map/',IncidentMap, name = 'IncidentMap'),]

from django.urls import path
from .views import IncidentMap

urlpatterns = [
    path('incident-map/', IncidentMap, name='IncidentMap'),
]

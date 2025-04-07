from django.urls import path
from .views import incidentMap

urlpatterns = [
    path('incident-map/', incidentMap, name='incidentMap'),
]

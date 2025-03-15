from django.urls import path
from . import views

#url configurations
urlpatterns = [
    path('alertsend/', views.locRec),
    path('alert/', views.showButton)
]

 
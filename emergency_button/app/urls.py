from django.urls import path
from django.views.generic import TemplateView
from .views import register_user
from . import views

# Consolidated URL configurations
urlpatterns = [
    path('', views.home, name='home'),
       
    path('registerUser/', views.register_user, name='register_user'),
     path('registration_success/', views.registration_success, name='registration_success'),
    path('login/', views.login_user, name='login_user'),

    path('alert/', views.showButton, name='show_alert'),
    path('alertsend/', views.trigger_emergency, name='send_alert'),
    path('alert/cancel/', views.cancel_emergency, name='cancel_emergency'),

    path('report/', views.report_incident, name='report_incident'),
    path('history/', views.report_history, name='report_history'),

    path('maps/', views.safety_resources, name= 'show_map'),

    path('resources/', views.safety_resources, name='safety_resources'),

]


from django.urls import path
from django.views.generic import TemplateView
from .views import register_user
from . import views

# Consolidated URL configurations
urlpatterns = [
    path('alertsend/', views.locRec),
    path('alert/', views.showButton),
    path('registerUser/', register_user, name='register_user'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('login/', views.login_user, name='login_user'),
    path('', views.home, name='home'),
]
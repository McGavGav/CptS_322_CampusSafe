from django.urls import path
from crimoapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resources/', views.resources, name='resources'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/', views.report, name='report'),
    path('registerUser/', views.register_user, name='register_user'),  # Fixed import
    path('registration_success/', views.registration_success, name='registration_success'),
    path('login/', views.login_user, name='login_user'),  # Add login view
    path('incident-map/', incidentMap, name='incidentMap'),
]

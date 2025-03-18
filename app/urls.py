from django.urls import path
from django.views.generic import TemplateView
from .views import register_user
from . import views

#url configurations
urlpatterns = [
    path('alertsend/', views.locRec),
    path('alert/', views.showButton),
    path('register/', register_user, name='register_user'),
    path('registration_success/', TemplateView.as_view(template_name="registration_success.html"), name='registration_success'),
]


 
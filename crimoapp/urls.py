from django.urls import path
from crimoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('resources/',views.resources,name='resources'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("report/", views.report, name="report"),
]

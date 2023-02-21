from django.contrib import admin
from django.urls import path, include 
from .views import Home, Prepare

urlpatterns = [
   path('Home',Home, name='Home' ),
   path('Prepare',Prepare, name='Prepare' ),
    
]

from django.contrib import admin
from django.urls import path, include 
from .views import Home

urlpatterns = [
   path('Home',Home, name='Home' ),
    
    
]

from django.urls import include, path
from .views import contactus

urlpatterns = [
    # path('add/', add_user, name='add_user'),
    path('ContactUs', contactus, name='contactus')
    
]


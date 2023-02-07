from django.urls import include, path
from .views import add_user

urlpatterns = [
    path('add/', add_user, name='add_user'),
    path('', include('userapp.urls')),
]


from django.shortcuts import render

# Create your views here.

import requests

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={'086b10858db32a1f21b26efeef0ae98b'}&units=metric"
    response = requests.get(url)
    data = response.json()
    weather = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
    }
    return weather

def weather(request):
    city = request.GET.get('city')
    if city:
        weather = get_weather(city)
    else:
        weather = None
    context = {
        'weather': weather,
    }
    return render(request, 'weather_app\\updates.html', context)




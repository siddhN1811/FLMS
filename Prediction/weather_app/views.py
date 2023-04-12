from django.shortcuts import render
from django.core.mail import send_mail
from Prediction import settings
# Create your views here.

import requests
import model

def forecast():
        
        
# Getting next day's forecast data ------------

    url2 = "https://api.openweathermap.org/data/2.5/forecast?q=mumbai&units=imperial&appid=086b10858db32a1f21b26efeef0ae98b"
    response2 = requests.get(url2)
    dataTomorrow = response2.json()

    # predict_value = {
    #     'temperature': data['main']['temp'],
    #     'minTemperature': data['main']['temp_min'],
    #     'maxTemperature': data['main']['temp_max'],
    #     'feelsLike': data['main']['feels_like'],
    #     'humidity':data['main']['humidity'],
    #     'wind':data['wind']['deg']

    # }

#forecast data-----------------
    predict_tomorrow = {

        'temp_max':round(((dataTomorrow['list'][1]['main']['temp_max'] -32)*5)/9,2),
        'temp_min':round(((dataTomorrow['list'][1]['main']['temp_min'] -32)*5)/9,2),
        'temp':round(((dataTomorrow['list'][1]['main']['temp'] -32)*5)/9,2),
        'feels_like':round(((dataTomorrow['list'][1]['main']['feels_like'] -32)*5)/9,2),
        'humidity':dataTomorrow['list'][1]['main']['humidity'],
        'wind':dataTomorrow['list'][1]['wind']['deg']
    }
    
# #forcast values to pass to model.predict---------

    val = [list(predict_tomorrow.values())]

    return val

    
# a = forecast()

# # Prediction--------------
# prediction  = model.predict(a)
# return prediction

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q=mumbai&units=imperial&appid=086b10858db32a1f21b26efeef0ae98b"
    response = requests.get(url)
    data = response.json()


    weather = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
        'humidity':data['main']['humidity'],
        'pressure':data['main']['pressure'],

    }
    weather['temperature'] = ((weather['temperature'] -32)*5)/9
    weather['temperature'] = str(float("{:.2f}".format(weather['temperature'])))+'°'+'C'
    return weather



def weather(request):
    # city = request.GET.get('city')
    # if city:
    weather = get_weather('Mumbai')
    # else:
        # weather = None
    a = forecast()
    # Prediction--------------
    prediction  = model.predict(a)
    # print(prediction)
    # prediction=100
    # if prediction>90:
    #     send_mail(
    #     'Flood Warning!!',
    #     'There is a high chance of flood occuring tomorow, so follow the guidlines on the preparing for floods page',
    #     settings.EMAIL_HOST_USER,
    #     ['kalpita@dbit.in'],
    #     fail_silently=False,
    #     )
    #     print("Sent successfully")
    context = {
        'weather': weather,
        'prediction': prediction
    }
    return render(request, 'weather_app\\updates.html', context)



a = forecast()

prediction  = model.predict(a)
print(prediction)





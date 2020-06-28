from django.shortcuts import render
from django.shortcuts import render,redirect
import requests
import datetime
from django.contrib import messages

def weather(request):

 if request.method == 'POST':
    city2=request.POST['weather']
    context=""
    url = f'https://api.openweathermap.org/data/2.5/weather?appid=40888a894484a9c947653e53e5c61f72&q={city2}'
    url_checker=requests.get(url)
    if url_checker.status_code==200:
        r = requests.get(url).json()
        city_weather = {
            'city': city2,
            'temp':int( r['main']['temp'])-272,
            'des': r['weather'][0]['main'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'min': int(r['main']['temp_min'])-272,
            'max': int(r['main']['temp_max'])-272,
            'feels': int(r['main']['feels_like'])-272,
            'wind': r['wind']['speed'],
            'pressure': r['main']['pressure'],
            'country': r['sys']['country'],
        }
        context = {'city_weather': city_weather}
        return render(request, 'weather_final.html', context)
    else :
        messages.info(request, 'city is not found')
        return redirect('weather:w')

 location_url='https://ipinfo.io/'
 location_data=requests.get(location_url).json()
 city2=location_data['city']
 url = f'https://api.openweathermap.org/data/2.5/weather?appid=40888a894484a9c947653e53e5c61f72&q={city2}'
 r = requests.get(url).json()

 city_weather = {
     'city': city2,
     'temp': int(r['main']['temp']) - 272,
     'des': r['weather'][0]['main'],
     'description': r['weather'][0]['description'],
     'icon': r['weather'][0]['icon'],
     'min': int(r['main']['temp_min']) - 272,
     'max': int(r['main']['temp_max']) - 272,
     'feels': int(r['main']['feels_like']) - 272,
     'wind': r['wind']['speed'],
     'pressure': r['main']['pressure'],
     'country': r['sys']['country'],
 }
 context = {'city_weather': city_weather}
 return render(request, 'weather_final.html',context)

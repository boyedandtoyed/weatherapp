import requests
from django.shortcuts import render

from .models import City
from .forms import CityModelForm


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5c3b622b508945cb2f5a05a0607de8a9'

    if request.method=='POST':
        form = CityModelForm(request.POST)
        form.save()
        
    form = CityModelForm()
    
    weather_data= [] 
    city_list = City.objects.all()
    
    for city in city_list:    
        response = requests.get(url.format(city)).json()
        city_weather = {
            "city": city.name,
            "temperature": response["main"]["temp"], 
            "description": response['weather'][0]['description'],
            "icon":response['weather'][0]['icon'],     
        }

        weather_data.append(city_weather)
        
    return render(request, 'weather/weather.html', {'weather_data':weather_data, 'form':form})
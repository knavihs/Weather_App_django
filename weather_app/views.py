from django.shortcuts import render,redirect
from .models import City
from .form import CityForm
import requests


# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=65ddfade9c9b27cfbcc56c19c84c5019'
    message = ''
    err_msg=''
    message_class = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['Name']
            r =requests.get(url.format(new_city)).json()
            if r['cod'] == 200:
                exist_count = City.objects.filter(Name=new_city).count()
                if exist_count == 0:
                    form.save()
                    message = "Showing weather result "
                    message_class = "alert-success"
                else:
                    message = "Data for the selected city already available"
                    message_class = "alert-warning"
            else:
                message="Invalid City, or check the spelling of the city"
                message_class="alert-danger"

    form = CityForm()
    weather_data=[]

    cities = City.objects.all()
    for city in cities:
        r = requests.get(url.format(city)).json()
        print(r)
        city_weather={
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context={
        'weather_data':weather_data,
        'form':form,
        'msg':message,
        'message_class':message_class
    }
    return render(request,'weather_app/weather.html',context)

def delete_city(request, city_name):
    City.objects.filter(Name=city_name).delete()
    return redirect('home')






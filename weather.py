# Application Programming Interface for OpenWeatherMap
import requests

def Weather(city):
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=6ec80f0d5076c60d3ffcbc20da2b269d&q='
    # city = input('Enter the City Name :')
    url = api_address + city
    json_data = requests.get(url).json()
    format_add = json_data['main']
    print(format_add)
    print("Weather {0} Temperature is mininum {1} Celcius and maximum {2} Celcius".format(
        json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))
    return format_add
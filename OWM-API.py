# weather forecast using openweather map api
import requests
import json

weather_icons = {
    '01d': '☀️',  # Sunny
    '01n': '🌙',  # Clear night
    '02d': '⛅',  # Few clouds
    '02n': '⛅',  # Few clouds
    '03d': '☁️',  # Scattered clouds
    '03n': '☁️',  # Scattered clouds
    '04d': '☁️',  # Broken clouds
    '04n': '☁️',  # Broken clouds
    '09d': '🌧️',  # Rain showers
    '09n': '🌧️',  # Rain showers
    '10d': '🌦️',  # Rain
    '10n': '🌦️',  # Rain
    '11d': '⛈️',  # Thunderstorm
    '11n': '⛈️',  # Thunderstorm
    '13d': '❄️',  # Snow
    '13n': '❄️',  # Snow
    '50d': '🌫️',  # Mist
    '50n': '🌫️',  # Mist
}

def get_weather(city):
    print("Weather forecast for "+city+":\n")
    url="https://api.openweathermap.org/data/2.5/weather?"
    api_key="b0fdaab1648df8b448f07dde33141cec"
    complete_url=url+"appid="+api_key+"&q="+city
    response=requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature=y["temp"]
        current_pressure=y["pressure"]
        current_humidity=y["humidity"]
        z=x["weather"]
        weather_description=z[0]["description"]
        icon=weather_icons[z[0]["icon"]]
        return ("Temperature (in kelvin unit) = " + str(current_temperature)+"\natmospheric pressure (in hPa unit) = "+str(current_pressure)+"\nhumidity (in percentage) = "+str(current_humidity)+"\ndescription = "+str(weather_description)+" "+icon)
    else:
        return "City not found"
    


while True:
    #menu driven program
    print("1. Get weather forecast\n2. Exit")
    choice=input("Enter choice: ")
    if int(choice.isdigit())==False:
        print("Invalid choice")
        continue
    else:
        choice=int(choice)
    if choice==1:
        city=input("Enter city name: ")
        ans=get_weather(city)
        print(ans)
    elif choice==2:
        break
    else:
        print("Invalid choice")
        continue

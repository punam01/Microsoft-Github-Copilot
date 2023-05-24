# weather forecast using openweather map api
import requests
import json

def get_weather_icon(code):
    if code == '01d':
        return '☀️'  # Sunny
    elif code == '01n':
        return '🌙'  # Clear night
    elif code == '02d' or code == '02n':
        return '⛅'  # Few clouds
    elif code == '03d' or code == '03n':
        return '☁️'  # Scattered clouds
    elif code == '04d' or code == '04n':
        return '☁️'  # Broken clouds
    elif code == '09d' or code == '09n':
        return '🌧️'  # Rain showers
    elif code == '10d' or code == '10n':
        return '🌦️'  # Rain
    elif code == '11d' or code == '11n':
        return '⛈️'  # Thunderstorm
    elif code == '13d' or code == '13n':
        return '❄️'  # Snow
    elif code == '50d' or code == '50n':
        return '🌫️'  # Mist
    else:
        return '❓'  # Unknown condition

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
        icon=get_weather_icon(z[0]["icon"])
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

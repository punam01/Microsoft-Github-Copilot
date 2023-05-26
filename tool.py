# weather forecast using openweather map api
import requests
import json
import datetime
from urllib.request import urlopen 

#declare global varibales
min_temperature=0
max_temperature=0
cloudiness=0
visibility=0
icon=""
weather_description=""
current_temperature=0
current_pressure=0
current_humidity=0
current_date_time=""
current_unix_time=0
city=""
longitude=""
latitude=""
wind_speed=0
wind_deg=0
sunrise=0
sunset=0
weather_description=""
current_city=""
current_country=""

#make a dictionary of above variables
weather_data={
    "min_temperature":min_temperature,
    "max_temperature":max_temperature,
    "cloudiness":cloudiness,
    "visibility":visibility,
    "icon":icon,
    "weather_description":weather_description,
    "current_temperature":current_temperature,
    "current_pressure":current_pressure,
    "current_humidity":current_humidity,
    "current_date_time":current_date_time,
    "current_unix_time":current_unix_time,
    "city":city,
    "longitude":longitude,
    "latitude":latitude,
    "wind_speed":wind_speed,
    "wind_deg":wind_deg,
    "sunrise":sunrise,
    "sunset":sunset,
    "weather_description":weather_description,
    "current_city":current_city,
    "current_country":current_country
}
    
#dictionary to store weather icons
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

#dictionary for country codes
country_codes={
    "AF":"Afghanistan",
    "AX":"Aland Islands",
    "AL":"Albania",
    "DZ":"Algeria",
    "AS":"American Samoa",
    "AD":"Andorra",
    "AO":"Angola",
    "AI":"Anguilla",
    "AQ":"Antarctica",
    "AG":"Antigua And Barbuda",
    "AR":"Argentina",
    "AM":"Armenia",
    "AW":"Aruba",
    "AU":"Australia",
    "AT":"Austria",
    "AZ":"Azerbaijan",
    "BS":"Bahamas",
    "BH":"Bahrain",
    "BD":"Bangladesh",
    "BB":"Barbados",
    "BY":"Belarus",
    "BE":"Belgium",
    "BZ":"Belize",

    "BJ":"Benin",
    "BM":"Bermuda",
    "BT":"Bhutan",
    "BO":"Bolivia",
    "BA":"Bosnia And Herzegovina",
    "BW":"Botswana",
    "BV":"Bouvet Island",
    "BR":"Brazil",
    "IO":"British Indian Ocean Territory",
    "BN":"Brunei Darussalam",
    "BG":"Bulgaria",
    "BF":"Burkina Faso",
    "BI":"Burundi",
    "KH":"Cambodia",
    "CM":"Cameroon",
    "CA":"Canada",
    "CV":"Cape Verde",
    "KY":"Cayman Islands",
    "CF":"Central African Republic",
    "TD":"Chad",
    "CL":"Chile",
    "CN":"China",
    "CX":"Christmas Island",
    "CC":"Cocos (Keeling) Islands",
    "CO":"Colombia",
    "KM":"Comoros",
    "CG":"Congo",
    "CD":"Congo, Democratic Republic",
    "CK":"Cook Islands",


    "CR":"Costa Rica",
    "CI":"Cote D'Ivoire",
    "HR":"Croatia",
    "CU":"Cuba",
    "CY":"Cyprus",
    "CZ":"Czech Republic",
    "DK":"Denmark",
    "DJ":"Djibouti",
    "DM":"Dominica",
    "DO":"Dominican Republic",
    "EC":"Ecuador",
    "EG":"Egypt",
    "SV":"El Salvador",
    "GQ":"Equatorial Guinea",
    "ER":"Eritrea",
    "EE":"Estonia",
    "ET":"Ethiopia",
    "FK":"Falkland Islands (Malvinas)",
    "FO":"Faroe Islands",
    "FJ":"Fiji",
    "FI":"Finland",
    "FR":"France",
    "GF":"French Guiana",
    "PF":"French Polynesia",
    "TF":"French Southern Territories",
    "GA":"Gabon",
    "GM":"Gambia",
    "GE":"Georgia",
    "DE":"Germany",
    "GH":"Ghana",
    "GI":"Gibraltar",
    "GR":"Greece",
    "GL":"Greenland",
    "GD":"Grenada",
    "GP":"Guadeloupe",
    "GU":"Guam",
    "GT":"Guatemala",
    "GG":"Guernsey",
    "GN":"Guinea",
    "GW":"Guinea-Bissau",
    "GY":"Guyana",
    "HT":"Haiti",
    "HM":"Heard Island & Mcdonald Islands",
    "VA":"Holy See (Vatican City State)",
    "HN":"Honduras",
    "HK":"Hong Kong",
    "HU":"Hungary",
    "IS":"Iceland",
    "IN":"India",
    "ID":"Indonesia",
    "IR":"Iran, Islamic Republic Of",
    "IQ":"Iraq",
    "IE":"Ireland"
}

#ditionary to store weather description
weather_description={
    "clear sky":"A clear sky is a weather condition characterized by an absence of clouds, resulting in a vast expanse of blue overhead. It is a sight that evokes a sense of openness and tranquility. During clear sky conditions, the sun shines brightly, casting a warm and radiant glow over the surroundings.",
    "few clouds":"A few clouds is a weather condition characterized by the presence of scattered clouds in the sky, without complete cloud cover. It is an intermediate state between a clear sky and an overcast sky, where some clouds are visible but do not obscure the entire sky.",
    "scattered clouds":"Scattered clouds is a weather condition characterized by clouds that are dispersed across the sky, but not covering the entire horizon. It represents a state where clouds are present in various parts of the sky, with significant gaps of clear or blue sky visible between them.",
    "broken clouds":"Broken clouds is a weather condition characterized by a sky that is partially covered with clouds. It represents a state where the cloud cover is extensive and fragmented, with significant gaps of clear sky visible between the cloud formations.",
    "shower rain":"Shower rains, also known as showers, refer to a type of precipitation characterized by short-lived bursts of rainfall. Showers are generally brief in duration but can vary in intensity, ranging from light drizzles to heavy downpours. Unlike continuous rainfall, which lasts for an extended period, showers are intermittent and often occur in a scattered or localized pattern.",
    "rain":"Rain is a form of precipitation in which water droplets fall from the atmosphere towards the Earth's surface. It is a vital component of the water cycle and plays a crucial role in sustaining life on our planet.",
    "moderate rain":"Moderate rain is a type of rainfall characterized by rainfall rates ranging from 2.5 mm to 7.6 mm (0.098 in to 0.299 in) per hour. It is heavier than drizzle but lighter than heavy rain, and falls in the form of small to medium-sized droplets.",
    "thunderstorm":"A thunderstorm is a weather phenomenon characterized by the presence of thunder, lightning, heavy rain, and sometimes gusty winds. It is a powerful and intense atmospheric event that occurs when there are strong updrafts of warm, moist air interacting with cooler air masses.",
    "snow":"Snow is a form of precipitation that occurs when water vapor freezes in the atmosphere and falls to the ground as ice crystals. It is a characteristic feature of colder climates and is associated with freezing temperatures.",
    "mist":"Mist is a weather condition characterized by the presence of tiny water droplets suspended in the air, reducing visibility to some extent. It is a type of atmospheric moisture that forms close to the ground when the air is saturated and near the dew point temperature.",
    "haze" :"Haze is a weather phenomenon characterized by the presence of fine particles, such as dust, smoke, or pollutants, in the air. It results in reduced visibility and a hazy or smoky appearance in the atmosphere.",
    "fog":"A dense cloud layer near the ground that severely restricts visibility.",
    "drizzle":"Light rain characterized by fine and numerous water droplets.",
    "snow":"Snow is a form of precipitation that occurs when water vapor freezes in the atmosphere and falls to the ground as ice crystals. It is a characteristic feature of colder climates and is associated with freezing temperatures.",
    "smoke":"Smoke is a collection of airborne solid and liquid particulates and gases emitted when a material undergoes combustion or pyrolysis, together with the quantity of air that is entrained or otherwise mixed into the mass.",
    "sand/ dust whirls":"A sand or dust whirl is a weather phenomenon characterized by a small rotating column of air over land, visible as a dust devil or sand whirl, respectively. It is a type of atmospheric vortex that forms when there is sufficient instability and wind shear in the lower atmosphere.",
    "sand":"Sand is a granular material composed of finely divided rock and mineral particles. It is defined by size, being finer than gravel and coarser than silt.",
    "dust":"Dust is a fine powder of solid matter, consisting of tiny particles of earth or waste matter lying on the ground or on surfaces or carried in the air.",
    "volcanic ash":"Volcanic ash consists of fragments of pulverized rock, minerals and volcanic glass, created during volcanic eruptions and measuring less than 2 mm (0.079 inches) in diameter.",
    "squalls":"A squall is a sudden, sharp increase in wind speed lasting minutes, contrary to a wind gust lasting seconds. They are usually associated with active weather, such as rain showers, thunderstorms, or heavy snow.",
    "tornado":"A tornado is a rapidly rotating column of air that is in contact with both the surface of the Earth and a cumulonimbus cloud or, in rare cases, the base of a cumulus cloud.",
    "light snow":"Light and gentle snowfall with small accumulation.",
    "moderate snow":"Moderate snowfall with accumulation of 2-5 cm.",
    "heavy snow":"Heavy snowfall with accumulation of 5-10 cm.",
    "overcast clouds":"Overcast clouds is a weather condition characterized by a sky that is completely covered with clouds. It represents a state where the cloud cover is extensive and continuous, with no gaps of clear sky visible between the cloud formations."

}
#function to get current loaction
def get_location():
    url="http://ipinfo.io/json"
    response=urlopen(url)
    data=json.load(response)
    city=data['city']
    return city

#function to get date day and time from unix timestamp
def get_date_time(timestamp):
    date=datetime.datetime.fromtimestamp(timestamp)
    return date.strftime('%H:%M:%S \n%A')   

#function to get weather forecast
def get_weather(city):
    print(city)
    url="https://api.openweathermap.org/data/2.5/weather?"
    api_key="b0fdaab1648df8b448f07dde33141cec"
    complete_url=url+"appid="+api_key+"&q="+city
    response=requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        weather_data["min_temperature"]=str(y["temp_min"])+ " K"
        weather_data["max_temperature"]=str(y["temp_max"])+" K"
        weather_data["cloudiness"]=str(x["clouds"]["all"])+" %"
        weather_data["visibility"]=str(x["visibility"])+" m"
        weather_data["current_temperature"]=str(y["temp"])+" K"
        weather_data["current_pressure"]=str(y["pressure"])+" hPa"
        weather_data["current_humidity"]=str(y["humidity"])+" %"
        weather_data["current_unix_time"]=x["dt"]
        weather_data["current_date_time"]=str(get_date_time(weather_data["current_unix_time"]))+" IST"
        z=x["weather"]
        i=z[0]["icon"]
        weather_data["icon"]=weather_icons[i]        
        weather_data["weather_description"]=weather_description[str(z[0]["description"])]
        wind=x["wind"]
        weather_data["wind_speed"]=str(wind["speed"])+" m/s"
        weather_data["wind_deg"]=str(wind["deg"])+" deg"
        weather_data["sunrise"]=str(get_date_time(x["sys"]["sunrise"]))+" IST"
        weather_data["sunset"]=str(get_date_time(x["sys"]["sunset"]))+" IST"
        weather_data["current_city"]=city
        coord=x["coord"]
        if(coord["lon"]>0):
            weather_data["longitude"]=str(coord["lon"])
        else:
            weather_data["longitude"]="Not Available"
        if(coord["lat"]>0):
            weather_data["latitude"]=str(coord["lat"])
        else:
            weather_data["latitude"]="Not Available"
        if(x["sys"]["country"] in country_codes):
            weather_data["current_country"]=country_codes[x["sys"]["country"]]
        else:
            weather_data["current_country"]=x["sys"]["country"]
        return weather_data
    else:
        print("City not found")
        return ""  


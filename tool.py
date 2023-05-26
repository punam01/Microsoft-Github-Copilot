# weather forecast using openweather map api
import requests
import json
import datetime
from urllib.request import urlopen 
import os
from dotenv import load_dotenv
    
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
    "KZ":"Kazakhstan",
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
    "IE":"Ireland",
    "RU":"Russia",
    "AU":"Australia",
    "IT":"Italy",
    "JP":"Japan",
    "KR":"Korea",
    "KP":"Korea, Democratic People'S Republic Of",
    "KW":"Kuwait",
    "KG":"Kyrgyzstan",
    "LA":"Lao People'S Democratic Republic",
    "LV":"Latvia",
    "LB":"Lebanon",
    "LS":"Lesotho",
    "LR":"Liberia",
    "LY":"Libyan Arab Jamahiriya",
    "LI":"Liechtenstein",
    "LT":"Lithuania",
    "LU":"Luxembourg",
    "MO":"Macao",
    "MK":"Macedonia",
    "MG":"Madagascar",
    "MW":"Malawi",
    "MY":"Malaysia",
    "MV":"Maldives",
    "ML":"Mali",
    "MT":"Malta",
    "MH":"Marshall Islands",
    "MQ":"Martinique",
    "MR":"Mauritania",
    "MU":"Mauritius",
    "YT":"Mayotte",
    "MX":"Mexico",
    "FM":"Micronesia, Federated States Of",
    "MD":"Moldova",
    "MC":"Monaco",
    "MN":"Mongolia",
    "ME":"Montenegro",
    "MS":"Montserrat",
    "MA":"Morocco",
    "MZ":"Mozambique",
    "MM":"Myanmar",
    "NA":"Namibia",
    "NR":"Nauru",
    "NP":"Nepal",
    "NL":"Netherlands",
    "AN":"Netherlands Antilles",
    "NC":"New Caledonia",
    "NZ":"New Zealand",
    "NI":"Nicaragua",
    "NE":"Niger",
    "NG":"Nigeria",
    "NU":"Niue",
    "NF":"Norfolk Island",
    "MP":"Northern Mariana Islands",
    "NO":"Norway",
    "OM":"Oman",
    "PK":"Pakistan",
    "PW":"Palau",
    "PS":"Palestinian Territory, Occupied",
    "PA":"Panama",
    "PG":"Papua New Guinea",
    "PY":"Paraguay",
    "PE":"Peru",
    "PH":"Philippines",
    "PN":"Pitcairn",
    "PL":"Poland",
    "PT":"Portugal",
    "PR":"Puerto Rico",
    "QA":"Qatar",
    "RE":"Reunion",
    "RO":"Romania",
    "RW":"Rwanda",
    "BL":"Saint Barthelemy",
    "SH":"Saint Helena",
    "KN":"Saint Kitts And Nevis",
    "LC":"Saint Lucia",
    "MF":"Saint Martin",
    "PM":"Saint Pierre And Miquelon",
    "VC":"Saint Vincent And Grenadines",
    "WS":"Samoa",
    "SM":"San Marino",
    "ST":"Sao Tome And Principe",
    "SA":"Saudi Arabia",
    "SN":"Senegal",
    "RS":"Serbia",
    "SC":"Seychelles",
    "SL":"Sierra Leone",
    "SG":"Singapore",
    "SK":"Slovakia",
    "SI":"Slovenia",
    "SB":"Solomon Islands",
    "SO":"Somalia",
    "ZA":"South Africa",
    "GS":"South Georgia And Sandwich Isl.",
    "ES":"Spain",
    "LK":"Sri Lanka",
    "SD":"Sudan",
    "SR":"Suriname",
    "SJ":"Svalbard And Jan Mayen",
    "SZ":"Swaziland",
    "SE":"Sweden",
    "CH":"Switzerland",
    "SY":"Syrian Arab Republic",
    "TW":"Taiwan",
    "TJ":"Tajikistan",
    "TZ":"Tanzania",
    "TH":"Thailand",
    "TL":"Timor-Leste",
    "TG":"Togo",
    "TK":"Tokelau",
    "TO":"Tonga",
    "TT":"Trinidad And Tobago",
    "TN":"Tunisia",
    "TR":"Turkey",
    "TM":"Turkmenistan",
    "TC":"Turks And Caicos Islands",
    "TV":"Tuvalu",
    "UG":"Uganda",
    "UA":"Ukraine",
    "AE":"United Arab Emirates",
    "GB":"United Kingdom",
    "US":"United States",
    "UM":"United States Outlying Islands",
    "UY":"Uruguay",
    "UZ":"Uzbekistan",
    "VU":"Vanuatu",
    "VE":"Venezuela",
    "VN":"Viet Nam",
    "VG":"Virgin Islands, British",
    "VI":"Virgin Islands, U.S.",
    "WF":"Wallis And Futuna",
    "EH":"Western Sahara",
    "YE":"Yemen",
    "ZM":"Zambia",
    "ZW":"Zimbabwe"

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
    "overcast clouds":"Overcast clouds is a weather condition characterized by a sky that is completely covered with clouds. It represents a state where the cloud cover is extensive and continuous, with no gaps of clear sky visible between the cloud formations.",
    "light rain":"Light rain is a type of rainfall characterized by rainfall rates ranging from 0.25 mm to 1 mm (0.01 in to 0.04 in) per hour. It is lighter than moderate rain but heavier than drizzle, and falls in the form of small to medium-sized droplets.",

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

#make a dictionary of above variables
weather_data={
    "longitude":"",
    "latitude":"",
    "icon":"",
    "main":"",
    "weather_description":"",
    "temp":"",
    "pressure":"",
    "humidity":"",
    "temp_min":"",
    "temp_max":"",
    "wind":"",
    "wind_speed":"",
    "wind_deg":"",
    "current_date_time":"",
    "current_unix_time":"",
    "sys":"",
    "sunrise":"",
    "sunset":"",
    "country":"",
    "cod":"", 
    "name":""
}
#function to parse weather api with missing data handling
def parse_weather_data(response):
    try:
        weather_data["longitude"]=response.get("coord",{}).get("lon")
        weather_data["latitude"]=response.get("coord",{}).get("lat")
        weather_data["icon"]=weather_icons[response["weather"][0]["icon"]]
        weather_data["weather_description"]=weather_description[response['weather'][0]['description']]
        weather_data["main"]=response.get("main")
        weather_data["temp"]=response.get("main",{}).get("temp")
        weather_data["pressure"]=response.get("main",{}).get("pressure")
        weather_data["humidity"]=response.get("main",{}).get("humidity")
        weather_data["temp_min"]=response.get("main",{}).get("temp_min")
        weather_data["temp_max"]=response.get("main",{}).get("temp_max")
        weather_data["wind"]=response.get("wind")
        weather_data["wind_speed"]=response.get("wind",{}).get("speed")
        weather_data["wind_deg"]=response.get("wind",{}).get("deg")
        weather_data["current_unix_time"]=response.get("dt")
        weather_data["current_date_time"]=get_date_time(weather_data["current_unix_time"])
        weather_data["sys"]=response.get("sys")
        weather_data["sunrise"]=get_date_time(response.get("sys",{}).get("sunrise"))
        weather_data["sunset"]=get_date_time(response.get("sys",{}).get("sunset"))
        weather_data["country"]=country_codes[response.get("sys",{}).get("country")]
        weather_data["name"]=response.get("name")
        weather_data["cod"]=response.get("cod")
        #handling missing data
        for key, value in weather_data.items():
            if value is None:
                print("Missing data for key: ", key)
                weather_data[key] = "N/A"  # Replace missing data with "N/A"
                print("\nReplaced with 'N/A'")
        print("\nWeather data:", weather_data)    
        return weather_data
    except KeyError:
        print("\nCity Not Found")
    

#function to get weather forecast
def get_weather(city):
    load_dotenv()
    url="https://api.openweathermap.org/data/2.5/weather?"
    api_key=str(os.getenv("API_KEY"))
    complete_url=url+"appid="+api_key+"&q="+city
    response=requests.get(complete_url)
    ans=parse_weather_data(response.json())
    return ans

#function to get weather forecast menu driven
def main():
    while True:
        print("\n\n\n1. Fetch weather information")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter a city name: ")
            get_weather(city)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

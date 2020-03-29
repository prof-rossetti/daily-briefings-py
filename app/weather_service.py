# app/weather_service.py

import os
import json
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
MY_ZIP = os.getenv("MY_ZIP", default="20057")
COUNTRY_CODE = os.getenv("COUNTRY_CODE", default="US")

def human_friendly_temp(my_temperature_f):
    """Rounds a decimal fahrenheit temperature to the nearest whole degree, adds degree symbol"""
    degree_sign = u"\N{DEGREE SIGN}"
    return f"{round(my_temperature_f)} {degree_sign}F"

# see: https://openweathermap.org/current
#weather_url = f"https://api.openweathermap.org/data/2.5/weather?zip={MY_ZIP},{COUNTRY_CODE}&appid={OPEN_WEATHER_API_KEY}"
request_url = f"https://api.openweathermap.org/data/2.5/forecast?zip={MY_ZIP},{COUNTRY_CODE}&units=imperial&appid={OPEN_WEATHER_API_KEY}"
response = requests.get(request_url)
parsed_response = json.loads(response.text)
#print(type(parsed_response)) #> dict
#print(parsed_response.keys()) #> dict_keys(['cod', 'message', 'cnt', 'list', 'city'])
#pprint(parsed_response)

city = parsed_response["city"]
#timezone = city["timezone"] #> -14400

print("-----------------")
print(f"TODAY'S WEATHER FORECAST FOR {city['name'].upper()}...")
print("-----------------")

for forecast in parsed_response["list"][0:9]:
    #print(forecast.keys()) #> dict_keys(['dt', 'main', 'weather', 'clouds', 'wind', 'sys', 'dt_txt'])
    #print("------")
    #pprint(forecast)
    #print("HOUR:", forecast["dt_txt"])
    #print("DESCRIPTION:", forecast["weather"][0]["description"].upper())
    #print("FEELS LIKE:", forecast["main"]["feels_like"], "(DEGREES F)")
    print(forecast["dt_txt"],
        "|",
        human_friendly_temp(forecast["main"]["feels_like"]),
        "|",
        forecast["weather"][0]["description"].upper(),
    )

#fcast = parsed_response["list"][0]

#breakpoint()

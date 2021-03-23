# app/weather_service.py

import os
import json
from pprint import pprint
from dateutil.parser import parse as parse_datetime

import requests
from dotenv import load_dotenv
from pgeocode import Nominatim as Geocoder
from pandas import isnull

from app import APP_ENV

load_dotenv()

COUNTRY_CODE = os.getenv("COUNTRY_CODE", default="US")
ZIP_CODE = os.getenv("ZIP_CODE", default="20057")


def get_hourly_forecasts(country_code, zip_code):
    """
    Fetches hourly forecast information from the Weather.gov API.

    Returns the forecast along with more information about the requested geography.

    Params:
        country_code (str) the requested country, like "US"
        zip_code (str) the requested postal code, like "20057"

    Example:
        geo, result = get_hourly_forecasts(country_code="US", zip_code="20057")
    """
    geocoder = Geocoder(country_code)
    geo = geocoder.query_postal_code(zip_code)
    #print(type(geocoder))
    #print(type(geo), geo)

    if isnull(geo.latitude) or isnull(geo.longitude): # we are using a special null-checking method from pandas because the geo is a pandas Series
        #print("INVALID GEOGRAPHY...")
        return geo, None

    request_url = f"https://api.weather.gov/points/{geo.latitude},{geo.longitude}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    #print(response.status_code)
    if response.status_code != 200:
        #print(parsed_response)
        return geo, None

    forecast_url = parsed_response["properties"]["forecastHourly"]
    forecast_response = requests.get(forecast_url)
    #print(forecast_response.status_code)
    if response.status_code != 200:
        #print(parsed_response)
        return geo, None

    parsed_forecast_response = json.loads(forecast_response.text)
    return geo, parsed_forecast_response

def format_temp(f):
    """
    Displays a fahrenheit temperature to the nearest whole degree, with a degrees symbol

    Params : f (float or int) temperature in fahrenheit
    """
    degree_sign = u"\N{DEGREE SIGN}"
    return f"{round(f)} {degree_sign}F"

def format_hour(dt_str):
    """
    Displays a datetime-looking string as the human friendly hour like "4pm"

    Params : dt_str (str) a datetime like "2021-03-29T21:00:00-04:00"
    """
    dt = parse_datetime(dt_str)
    #return dt.strftime("%I %p") #> "01 PM"
    return dt.strftime("%H:%M") #> "13:00"


if __name__ == "__main__":

    print(f"RUNNING THE WEATHER SERVICE IN {APP_ENV.upper()} MODE...")

    # CAPTURE INPUTS

    if APP_ENV == "development":
        user_country = input("PLEASE INPUT A COUNTRY CODE (e.g. 'US'): ")
        user_zip = input("PLEASE INPUT A ZIP CODE (e.g. 20057): ")
    else:
        user_country = COUNTRY_CODE
        user_zip = ZIP_CODE
    print("COUNTRY:", user_country)
    print("ZIP CODE:", user_zip)

    # FETCH DATA

    geo, result = get_hourly_forecasts(country_code=user_country, zip_code=user_zip)
    if not (geo.any() and result):
        print("INVALID GEOGRAPHY. PLEASE CHECK YOUR INPUTS AND TRY AGAIN!")
        exit()

    # DISPLAY OUTPUTS

    city_name = f"{geo.place_name}, {geo.state_code}"
    print("-----------------")
    print(f"TODAY'S WEATHER FORECAST FOR {city_name.upper()}...")
    print("-----------------")

    for forecast in result["properties"]["periods"][0:24]:
        #print(forecast.keys())
        #pprint(forecast)
        #breakpoint()
        print(format_hour(forecast["startTime"]), "|", format_temp(forecast["temperature"]), "|", forecast["shortForecast"])

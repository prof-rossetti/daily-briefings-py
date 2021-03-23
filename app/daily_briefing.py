# app/daily_briefing.py

import os
from dotenv import load_dotenv
from datetime import date

from app import APP_ENV
from app.weather_service import get_hourly_forecasts, set_geography, format_hour, format_temp
from app.email_service import send_email

load_dotenv()

USER_NAME = os.getenv("USER_NAME", default="Player 1")


if __name__ == "__main__":

    print(f"RUNNING THE DAILY BRIEFING APP IN {APP_ENV.upper()} MODE...")

    # CAPTURE INPUTS

    user_country, user_zip = set_geography()
    print("COUNTRY:", user_country)
    print("ZIP CODE:", user_zip)

    # FETCH DATA

    geo, result = get_hourly_forecasts(country_code=user_country, zip_code=user_zip)
    if not (geo.any() and result):
        print("INVALID GEOGRAPHY. PLEASE CHECK YOUR INPUTS AND TRY AGAIN!")
        exit()

    # DISPLAY OUTPUTS

    city_name = f"{geo.place_name}, {geo.state_code}"

    html = ""
    html += f"<h3>Good Morning, {USER_NAME}!</h3>"

    html += "<h4>Today's Date</h4>"
    html += f"<p>{date.today().strftime('%A, %B %d, %Y')}</p>"

    html += f"<h4>Weather Forecast for {city_name}</h4>"
    html += "<ul>"
    for forecast in result["properties"]["periods"][0:24]:
        hour = format_hour(forecast['startTime'])
        temp = format_temp(forecast['temperature'])
        html += f"<li>{hour} | {temp} | {forecast['shortForecast'].upper()}</li>"
    html += "</ul>"

    send_email(subject="[Daily Briefing] My Morning Report", html=html)


# web_app/routes/home_routes.py

from flask import Blueprint, render_template, request, jsonify

from app.weather_service import get_hourly_forecasts

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather/form")
def weather_form():
    print("VISITED THE WEATHER FORM...")
    return render_template("weather_form.html")

@weather_routes.route("/weather/forecast", methods=["GET", "POST"])
def weather_forecast():

    #if request.method == "POST":
    #    print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057', 'country_code': 'US'}
    #    country_code = request.form["country_code"]
    #    zip_code = request.form["zip_code"]
    #elif request.method == "GET":
    #    print("URL PARAMS:", dict(request.args)) #> {'zip_code': '20057', 'country_code': 'US'}
    #    country_code = request.args["country_code"]
    #    zip_code = request.args["zip_code"]

    request_data = request.form or request.args
    request_data = dict(request_data)
    print("PROCESSING FORECAST REQUEST:", request.method, request_data)
    country_code = request_data["country_code"] or "US"
    zip_code = request_data["zip_code"]

    print("GENERATING A WEATHER FORECAST...")
    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
    print(results.keys())

    return render_template("weather_forecast.html", country_code=country_code, zip_code=zip_code, results=results)

@weather_routes.route("/weather/forecast.json", methods=["GET"])
def weather_forecast_api():
    request_data = dict(request.args)
    print("PROCESSING FORECAST REQUEST:", request.method, request_data)
    country_code = request_data["country_code"] or "US"
    zip_code = request_data["zip_code"]

    print("GENERATING A JSON RESPONSE...")
    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
    print(results.keys())

    return jsonify(results)

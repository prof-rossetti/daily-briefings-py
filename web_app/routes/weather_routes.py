
from flask import Blueprint, request, jsonify

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather/forecast.json")
def weather_forecast():
    print("WEATHER FORECAST...", dict(request.args))
    country_code = request.args.get("country_code") or "US"
    zip_code = request.args.get("zip_code") or "20057"
    return jsonify({
        "country_code": country_code,
        "zip_code": zip_code,
        "city_name": "TODO",
        "hourly_forecasts": []
    }) # some dummy / placeholder data

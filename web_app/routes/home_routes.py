# web_app/routes/home_routes.py

from flask import Blueprint, request, jsonify, render_template

from app.weather_service import get_hourly_forecasts

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def home_page():
    print("HOME PAGE")
    return render_template("index.html")

@home_routes.route("/about")
def about_page():
    print("ABOUT PAGE")
    return render_template("about.html")

@home_routes.route("/other")
def other_page():
    print("OTHER PAGE")
    try:
        console.log(any(request.args), any(request.args.values()))
        user_name = request.args["user_name"]
        header_message = f"Hello, {user_name}!"
    except:
        header_message = "Hello World!"
    return render_template("other.html", header_message=header_message)

#
# API
#

#@home_routes.route("/weather/forecast", methods=["GET", "POST"])
#def weather_forecast():
#    print("GENERATING A WEATHER FORECAST...")
#
#    if request.method == "POST":
#        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
#        zip_code = request.form["zip_code"]
#    elif request.method == "GET":
#        print("URL PARAMS:", dict(request.args)) #> {'zip_code': '20057'}
#        zip_code = request.args["zip_code"]
#
#    results = get_hourly_forecasts(zip_code)
#    print(results.keys())
#    return render_template("weather_forecast.html", zip_code=zip_code, results=results)


#books = [
#    {"id": 1, "title": "Harry Potter I"},
#    {"id": 2, "title": "Harry Potter II"},
#    {"id": 3, "title": "Harry Potter III"},
#] # we'd normally make a database call or fetch some data
#
#@home_routes.route("/api/books")
#@home_routes.route("/api/books.json")
#def books_endpoint():
#    print("BOOKS...")
#    print(books)
#    return jsonify(books)
#
#@home_routes.route("/api/books/<book_id>")
#@home_routes.route("/api/books/<book_id>.json")
#def book_endpoint(book_id):
#    print("BOOK ID:", book_id)
#    try:
#        matching_book = [book for book in books if str(book["id"]) == str(book_id)][0]
#        return jsonify(matching_book)
#    except:
#        message = f"Oh, couldn't find a book with id '{book_id}'. Please try again."
#        return jsonify({"message": message}), 404
#
#
##@home_routes.route("/api/v0/book.json")
##def book_search_endpoint_v0():
##    url_params = dict(request.args)
##    print("URL PARAMS:", url_params)
##    #return jsonify({"message": "HERE IS YOUR BOOK (TODO)", "url_params": url_params})
##
##    print("BOOK ID:", book_id)
##    try:
##        matching_book = [book for book in books if str(book["id"]) == str(book_id)][0]
##        return jsonify(matching_book)
##    except:
##        message = f"Oh, couldn't find a book with id '{book_id}'. Please try again."
##        return jsonify({"message": message}), 404

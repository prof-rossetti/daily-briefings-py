# hello.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    print("HOME...")
    return "Welcome Home"

@app.route("/about")
def about():
    print("ABOUT...")
    return "About Me"

@app.route("/hello")
@app.route("/hello.json")
def hello_world():
    print("HELLO...", dict(request.args))
    name = request.args.get("name") or "World"
    message = f"Hello, {name}!"

    if ".json" in request.url:
        return jsonify({"message": message})
    else:
        return message

@app.route("/api/books")
@app.route("/api/books.json")
def list_books():
    print("BOOKS...")
    books = [
        {"id": 1, "title": "Book 1", "year": 1957},
        {"id": 2, "title": "Book 2", "year": 1990},
        {"id": 3, "title": "Book 3", "year": 2031},
    ] # some dummy / placeholder data
    return jsonify(books)

@app.route("/api/books/<int:book_id>")
@app.route("/api/books/<int:book_id>.json")
def get_book(book_id):
    print("BOOK...", book_id)
    book = {"id": book_id, "title": f"Example Book", "year": 2000} # some dummy / placeholder data
    return jsonify(book)





@app.route("/weather/forecast.json")
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

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

@app.route("/api/books.json")
def list_books():
    print("BOOKS...")
    books = [
        {"title": "Book 1", "year": 1957},
        {"title": "Book 2", "year": 1990},
        {"title": "Book 3", "year": 2031},
    ]
    return jsonify(books)

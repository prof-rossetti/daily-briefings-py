# hello.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/newpath")
def new_route():
    return "New Path"

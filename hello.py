# hello.py (root dir)
# following along with Prof for minimal flask app

from flask import Flask

app = Flask(__name__)

#route: a URL path to visit
#route function names should be unique
#ie. hello_world() v about()

@app.route("/")
def hello_world():
    print("VISITED THE HELLO PAGE")
    return "Hello, World"

@app.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return "About me!"


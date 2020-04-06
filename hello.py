# hello.py (root dir of repo)

from flask import Flask


app = Flask(__name__)

# route is like a url path to visit
@app.route("/")
def hello_world():
    print("VISITED THE HELLO PAGE")
    return "Hello, World!"

@app.route("/about")
def about():
    PRINT("VISITED THE ABOUT PAGE")
    return "About me!"
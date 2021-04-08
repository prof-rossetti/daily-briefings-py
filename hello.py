from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("VISITED THE HOME PAGE")
    return "Hello, World!"

@app.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return "About me!"

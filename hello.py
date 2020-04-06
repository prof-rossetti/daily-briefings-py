# my_app.py (root dir of repo)


from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/about")
def about():
    return "About me"
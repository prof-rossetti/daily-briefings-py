from flask import Flask
app = Flask(__name__)

# route: aka a URL path to visit 
# route function names should be unique (hello_world() vs about()
@app.route('/')
def hello_world():
    print("visited the home page")
    return 'Hello, World!'

@app.route('/about')
def about():
    print("visited the about page")
    return 'About me'
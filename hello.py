from flask import Flask
app = Flask(__name__)

# a route is essentially a route to visit 

@app.route("/")
def hello_world():
    print("VISITED THE HELLO PAGE")
    return 'Hello, World!'

# route function names should be unique - hello world vs. about
@app.route("/about")
def about_me():
    print("VISITED THE ABOUT PAGE")
    return 'About me!'

# for any changes that need to be reflected you need to stop 
# your web server and start it again
# you stop it with ctrl + c

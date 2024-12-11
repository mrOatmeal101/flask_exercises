# 1st step was to setup Virtual Enviornment inside the flask-greet-calc folder to keep a clean work environment. 
# then I created and updated the requirements.txt so that all of the individual packages where installed
# next i updated the git.ignore file so that the venv would not be added to my local git.
# followed by creating the app.py file with: touch app.py

# first line of code is to import Flask from the module flask 
from flask import Flask
from operations import add, sub, mult, div

# to create the flask application or instantiate it with app = Flask(__name__)
# this is a class and it makes us an app object.
# we store it in a variable called app.
app = Flask(__name__)
# then in the command line: flask run
# The server is now running and use ctrl + c to quit.
# if the file was called my_app.py, you would need to run the command, while in the VE:
    # FLASK_AAP=my_app.py flask run
# Set export FLASK EVN=development in my bash profile. 
# Also installed the debugger under the requirements.

@app.route('/')
def home_page():
    return "hello"

# now making the four different routes
@app.route('/add')
def addition(a,b):
    return add(10,30)

@app.route('/sub')
def sub(a, b):
    """Substract b from a."""
    return a - b

@app.route('/mult')
def mult(a, b):
    """Multiply a and b."""
    return a * b

@app.route('/div')
def div(a, b):
    """Divide a by b."""
    return a / b
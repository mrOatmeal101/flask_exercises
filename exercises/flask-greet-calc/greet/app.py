# 1st step was to setup Virtual Enviornment inside the flask-greet-calc folder to keep a clean work environment. 
# then I created and updated the requirements.txt so that all of the individual packages where installed
# next i updated the git.ignore file so that the venv would not be added to my local git.
# followed by creating the app.py file with: touch app.py

# first line of code is to import Flask from the module flask 
from flask import Flask

# to create the flask application or instantiate it with app = Flask(__name__)
# this is a class and it makes us an app object.
# we store it in a variable called app.
app = Flask(__name__)
# then in the command line: flask run
# The server is now running and use ctrl + c to quit.
# if the file was called my_app.py, you would need to run the command, while in the VE:
    # FLASK_AAP=my_app.py flask run
# Set export FLASK EVN=development in my bash profile. 
# Also installed the debugger under the requirements.txt 

# when then route, i.e. map the url /welcome.
# we are listening for a request for /welcome.
# tthe @ also makes it a decorator so it is expecting a function immediately after it. 
@app.route('/welcome')
# next is to add a view function, which is a function that returns web responses
def say_welcome():
    # this will now auto generate a full HTTP respone that has the text welcome on a web browers tab.
    # all the status codes, response headers, and everything else is auto generated. 
    return "welcome"

@app.route('/welcome/home')
def say_welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def say_welcome_back():
    return "welcome back"

# ----------------------------------------------------------------------
# Ran 3 tests in 0.006s

# OK
# Step one to create a web server with Flask is to import it.
from flask import Flask

# next step is to make a variable called app and set it equal to Flask(__name__)
app = Flask(__name__)

# This is telling python to let Flask run in this file.
# In the terminal then type | flask run | then the server will start
# CTRL + C is how to quit the server. 

# This is how you set the home directory or the home page or root directory
@app.route('/')
def home_page():
    html = """
    <html>
        <body>
        <h1>Home Page</h1>
            <p>smimple server example using flask</p>
            <a href = '/hello'>Go to hello page</a> 
        </body>
    </html>
    """
    return html

# can format it in html
@app.route('/hello')
def say_hello():
    html = """
    <html>
        <body>
        <h1>Hello!</h1>
            <p>this is the hello page</p>
        </body>
    </html>
    """
    return html

# simple example of a webpage
@app.route('/goodbye')
def say_goodbye():
    return 'goodbye there'


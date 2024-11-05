# Step one to create a web server with Flask is to import it.
from flask import Flask, request

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

@app.route('/search')
def search():
    # print(request.args) # ImmutableMultiDict([]) is the output in the terminal which is like an empty obj
    
    # if you type something into the search bar like:
    # http://127.0.0.1:5000/search?term=dog&start=top
    # it will now output this in the terminal:
    # ImmutableMultiDict([('term', 'dog'), ('start', 'top')]) 
    # now obj has key and values pairs
    # return 'search page'
    # after commenting out the print(request.args) and return 'search page' you can set the term to be equal to something
    # use term to find db data that matches term
    term = request.args['term']
    sort = request.args['sort'] # will now require sort in the web browers link. 
    return f'<h1>Search Results For: {term}</h1> <p>Sorting by: {sort}</p>' 
    # so if you input http://127.0.0.1:5000/search?term=cat&start=top
    # it will output Search Results For: cat
    # so now if you input: http://127.0.0.1:5000/search?term=cat&sort=top
    # you will get Search Results For: cat Sorting by: top
    # if you tried with start=top you will get an error. 
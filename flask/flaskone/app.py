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

# @app.route('/post', methods= ['POST', "GET"])
# def post_demo():
#     return 'you made a post request' # you need "GET" or it will now allow you to access it. 
# output on the web page is: you made a post request, which is a lie as you made a GET request. 

# to make an actual POST request: you type | curl -X POST http://127.0.0.1:5000/post
    # make sure your server is running and type this into a new ubuntu window. 
    # you made a post requestmroatmeal@TinyOat:~/Sect_19/19.1_FlaskIntro/flask/flaskone$ is the output on the terminal.
# you can seperate the POST and GET methods to:
# @app.route('/post', methods= ['POST'])
# def post_demo():
#     return 'you made a POST request'

# @app.route('/post', methods= ['GET'])
# def post_demo():
#     return 'you made a GET request'

# To serve a form:
@app.route('/add-comment')
def add_comment_form():
    return """
    <h1>Add Comment</h1>
    <form method="POST">
        <input type='text" placeholder='comment' name='comment'/>
        <input type='text" placeholder='username' name='username'/>
        <button>Submit</button>
    </form>
"""

# this is what happens after you hit the submit button
@app.route('/add-comment', methods= ['POST'])
def save_comment():
    comment= request.form['comment'] # this is refering to the name='comment' in the /add-comment route above. 
    # print(request.form)
    username = request.form['username']
    return f"""
    <h1>Saved Your Comment with the text of</h1>
    <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment}</li>
    </ul>
    """

# so now after you type something into the input box and hit submit you will get:
# Saved Your Comment with the text of: cat # i typed in cat in the comment box. 
# afer you at the username plachoder: and type james into the input box 
# you will get this on the terminal side:
# ImmutableMultiDict([('comment', 'i like cats'), ('comment', 'james')])
# and this on the web browser side(i typed i like cats):
# Saved Your Comment with the text of: i like cats
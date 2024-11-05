# Section 1 Flask Introduction Handout
# Whatever company you work at will want you to know a Python development framework. 
# Flask is one of the two most popular Python web frameworks, and it’s far more user-friendly than the other contender Django. 
# Reddit, Netflix, Lyft, Pinterest, and Airbnb all use Flask in their stack.

# If you want to build a web application, you need to use a framework to do that. 
# Web frameworks are a collection of the foundational tools necessary for web development. 
# Flask maps URLs to the code they are requesting, connects to a database, creates and serves up customizable HTML templates, 
# stores state information in a session, provides testing and debugging tools, and much much more. 

# In this subunit, you'll learn how to use the Flask framework. 
# Flask is what is called a microframework, which means that it provides more minimalistic functionality than an enterprise framework.

# Section 2
# python, js, html, cs & all the other langs, are the building blocks to making a web page.
# Flask is a framework that allows you to use these building blocks to make web pages.

# Goals - Web Development with Python
# Describe the purpose and responsibilities of a web framework
# Build small web applications using Python and Flask
# Set environmental variables for local Flask development
# Handle GET and POST requests with Flask
# Extract data from different parts of the URL with Flask

# Section 3 Introduction to Web Servers
# Flask will be your first back-end web framework.
#  Web Frameworks
# A Quick Demo
    # (venv) $ FLASK_ENV=development flask run
    # * Environment: development
    # * Debug mode: on
    # * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    # * Restarting with stat
    # * Debugger is active!
    # * Debugger PIN: 160-080-703

# What is a Web Server?
# A program that’s running on a machine and waiting for a web request.
# Note: A web server is a technology that can process requests and issue responses via HTTP, a protocol used to distribute 
# information on the world wide web. Though it’s also used to refer to computer systems and even internet “appliances,” we’ll 
# use web server to refer to the software running on a machine that’s waiting to respond to HTTP requests.

# Request
# web browser --GET/--> Web Server (app.py)
# The server then responds with the exact HTML text for that page:

# Response
# Web Browser <--String of HTML <html>..<html> -- Web Server (app.py)

# Section 4 Flask and Other Frameworks
# Flask is the tool we will be using in python to create web servers. 
# it is possible to create web server w/o a framework but it is very time consumming. 

# Flask is a Web Framework
# Set of functions, classes, etc. that help you define
    # Which requests to respond to
        # http://server/about-us
        # http://server/post/1
    # How to respond to requests
        # Shows an “About Us” page
        # Show the 1st blog post
# Like a library, but bigger and more opinionated, i.e. has rules and a structure you need to follow.
# Usage is similar to the Python Standard Library.

# Using the Python Standard Library
# from random import choice, randint
 
# Using Flask
# from flask import Flask, request

# What Do Web Applications Need To Do?
    # handle web requests
    # produce dynamic HTML
    # handle forms
    # handle cookies
    # connect to databases
    # provide user log-in/log-out
    # cache pages for performance
    # & more!

# Section 5 Our First Server
# Flask is a lightweight Python framework for web applications that provides the basics for URL routing and page rendering.

# Flask is called a "micro" framework because it doesn't directly provide features like form validation, 
# database abstraction, authentication, and so on. Such features are instead provided by special Python packages called Flask extensions. 
# The extensions integrate seamlessly with Flask so that they appear as if they were part of Flask itself. 
# For example, Flask doesn't provide a page template engine, but installing Flask includes the Jinja templating engine by default.
# For convenience, we typically speak of these defaults as part of Flask.

# In this video we first started a virtual enviornment inside a new folder called flask. 
# did this by typing | python3 -m venv venv | this creates the folder venv and makes it a virtual enviroment.
# Activated it by typing | source venv/bin/activate |
# Then installed flask in the virtual enviorment with the command | pip install flask |
# Made a file called app.py beacause that is the name that flask is expecting for a file name. 
    # you can give it another name but you will have to edit things. 

# In the file app.py we typed this. 
# Step one to create a web server with Flask is to import it.
# from flask import Flask

# next step is to make a variable called app and set it equal to Flask(__name__)
# app = Flask(__name__)

# This is telling python to let Flask run in this file.
# In the terminal then type | flask run | then the server will start
# CTRL + C is how to quit the server. 
# by default, the server, is in production mode and debug is off. 
# by copying and pasting http://127.0.0.1:5000 which was created after we typed flask run,
# into the web browser we will get the Not Found page with: 
# The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.

# the terminal will also show that there were request to the server:
# 127.0.0.1 - - [05/Nov/2024 10:10:44] "GET / HTTP/1.1" 404 -
# 127.0.0.1 - - [05/Nov/2024 10:10:44] "GET /favicon.ico HTTP/1.1" 404 -

# if you ctrl+c out of the server and try to visit in browser, it will now show the site can't be reached.

# If your Flask app file isn’t called app: 
# (venv) $ FLASK_APP=app.py flask run
# FLASK_APP=app.py is passing an “environmental variable”
# Only has this meaning while this program is running

# Section 6 Development Mode
# Development Mode
# Better to run Flask in “development mode”:

# Much better error messages
# Automatically re-loads server when code changes on disk
# Both of these are very helpful when developing–and very bad for working on a live, production server.
# (venv) $ FLASK_ENV=development flask run

# Setting Environmental Variables
# Can set FLASK_DEV once per terminal session:
# (venv) $ export FLASK_ENV=development | this line will make it so you dont have to type FLASK_ENV=development flask run every time you run the server.
# though if you go to another window or quit the server you will have to retype | export FLASK_ENV=development | in the new window.
# Add that line to shell config to run on every new terminal session.

# Or you can configure your .profile which is in the root directory file to always run in development mode. 
# just paste export FLASK_ENV=development  & export FLASK_DEBUG=1 at the bottom of the file and save and close.

# Section 7 Adding Routes
# One of the core concepts of back-end web development is writing code that listens for HTTP requests and acts in response to them.
# listening for a request from /dogs /whatever

# Making Responses
# A function that returns web response is called a view

# Response is a string
# Usually, a string of HTML
# So, our function returns an HTML string:

# @app.route('/hello')
# def say_hello():
#     """Return simple "Hello" Greeting."""

#     html = "<html><body><h1>Hello</h1></body></html>"
#     return html

# So on the app.py file we added
    # @app.route('/hello')
    # def say_hello():
    #     return 'hello there'
# so that when we go to the web browser and type: http://127.0.0.1:5000/hello
# the web page now displays 'hello there' in the top left corner. 
# flask is taking care of the http request - it is setting the status code and making the text a header. 

# More detail on how flask works and how you get an html style web page back. 
# Flask Files Determine HTTP Response: The route handlers and templates you define in your Flask application determine what 
# content is included in the HTTP response.

# Dynamic Responses: Flask allows for both static responses (plain text or HTML) and dynamic responses (using templates) based on 
# user input or other data.

# Structured Communication: Flask handles the entire communication process, responding to HTTP requests with the appropriate 
# content and structure as defined in your application code.

# Jinja2 is a powerful templating engine that enables developers to create dynamic HTML pages easily. 
# It combines static HTML with Python logic, allowing for the generation of dynamic content based on user data or other parameters. 
# Its features like variable interpolation, control structures, template inheritance, filters, and macros make it an essential tool for 
# building web applications with Flask and other frameworks.

# all of the below are static/hard coded routes but you can use dynamic routes. 
# This is how you set the home directory or the home page or root directory
# @app.route('/')
# def home_page():
#     html = """
#     <html>
#         <body>
#         <h1>Home Page</h1>
#             <p>smimple server example using flask</p>
#             <a href = '/hello'>Go to hello page</a> 
#         </body>
#     </html>
#     """
#     return html

# # can format it in html
# @app.route('/hello')
# def say_hello():
#     html = """
#     <html>
#         <body>
#         <h1>Hello!</h1>
#             <p>this is the hello page</p>
#         </body>
#     </html>
#     """
#     return html

# # simple example of a webpage
# @app.route('/goodbye')
# def say_goodbye():
#     return 'goodbye there'

# Section 8 Query String Parameters
# You know what a query string is: data that comes into a URL via a GET request.
# This video will show you how Reddit and Google handle incoming query strings on the back-end.

# GET and POST
# Requests
# Flask provides an object, request, to represent web requests
    # from flask import request

# Handling Query Arguments
# For a url like /search?term=fun
# @app.route("/search")
# def search():
#     """Handle GET requests like /search?term=fun"""

#     term = request.args["term"]
#     return f"<h1>Searching for {term}</h1>"

# this is what was covered in the video:

# @app.route('/search')
# def search():
#     # print(request.args) # ImmutableMultiDict([]) is the output in the terminal which is like an empty obj
    
#     # if you type something into the search bar like:
#     # http://127.0.0.1:5000/search?term=dog&start=top
#     # it will now output this in the terminal:
#     # ImmutableMultiDict([('term', 'dog'), ('start', 'top')]) 
#     # now obj has key and values pairs
#     # return 'search page'
#     # after commenting out the print(request.args) and return 'search page' you can set the term to be equal to something
#     # use term to find db data that matches term
#     term = request.args['term']
#     sort = request.args['sort'] # will now require sort in the web browers link. 
#     return f'<h1>Search Results For: {term}</h1> <p>Sorting by: {sort}</p>' 
#     # so if you input http://127.0.0.1:5000/search?term=cat&start=top
#     # it will output Search Results For: cat
#     # so now if you input: http://127.0.0.1:5000/search?term=cat&sort=top
#     # you will get Search Results For: cat Sorting by: top
#     # if you tried with start=top you will get an error. 

# Section 9

# Section 10

# Section 11




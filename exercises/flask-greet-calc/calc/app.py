# 1st step was to setup Virtual Enviornment inside the flask-greet-calc folder to keep a clean work environment. 
# then I created and updated the requirements.txt so that all of the individual packages where installed
# next i updated the git.ignore file so that the venv would not be added to my local git.
# followed by creating the app.py file with: touch app.py

# first line of code is to import Flask from the module flask 
from flask import Flask, request
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

# needed to acess information from the query string, which in this case a = 10 & b= 20.
# starts with ? and has key value pairs combined with & 
# ?a=10&b=20
# imported request the built in object from flask library.
@app.route('/')
def home_page():
    return f"<h1>Home Page</h1>"

@app.route('/search')
def search():
    term = request.args['term']
    return f"<h1>Search for: {term}</h1>"

# now making the four different routes which are all GET request. 
# to use request, type request.args['name_of_term']
@app.route('/add')
def addition():
    """Adding keyword arguments a and b."""
    # need to turn a and b into intergers, otherwise will be read as strings
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = add(a,b)
    return f'{total}'

@app.route('/sub')
def subtraction():
    """Subtracting keyword arguments a and b."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = sub(a,b)
    return f'{total}'

@app.route('/mult')
def multiply():
    """Multipling keyword arguments a and b."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = mult(a,b)
    return f'{total}'

@app.route('/div')
def divide():
    """Dividing keyword arguments a and b."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = div(a,b)
    return f'{total}'

# Now make a variable route so that the above routes can be compressed into one.
# To do this take variable name and wrap in <>.
# when you wrap the variable, flask takes it and plugs into function as a keyword argument.
# the keyword argument needs to match exactly the wraped text. 
# @app.route('/math/<operation>')
# def math_op(operation):
#     """Addition on keyword arguments a and b."""
#     if operation == 'add':
#         a = int(request.args['a'])
#         b = int(request.args['b'])
#         total = add(a,b)
#         return f'{total}'
    
#     if operation == 'sub':
#         """Subtracting keyword arguments a and b."""
#         a = int(request.args['a'])
#         b = int(request.args['b'])
#         total = sub(a,b)
#         return f'{total}'
    
#     if operation == 'mult':
#         """Multipling keyword arguments a and b."""
#         a = int(request.args['a'])
#         b = int(request.args['b'])
#         total = mult(a,b)
#         return f'{total}'
    
#     if operation == 'div':
#         """Dividing keyword arguments a and b."""
#         a = int(request.args['a'])
#         b = int(request.args['b'])
#         total = div(a,b)
#         return f'{total}'

# without the if statements and pulling operations from a python dictionary
ops = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
    }

@app.route("/math/<operation>")
def do_math(operation):
    """Math operations on keyword arguments a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = ops[operation](a, b)

    return f"{total}"
# # Exercises
# flask-greet-calc/
#   greet/
#   calc/
# At the top level of this (inside flask-greet-calc), create a virtual environment:

# (env) $ git status
# Greet
# In the greet folder, Make a simple Flask app that responds to these routes with simple text messages:

# /welcome
# Returns “welcome”
# /welcome/home
# Returns “welcome home”
# /welcome/back
# Return “welcome back”
# Once you’ve finished this, run the tests for it:

# $ python3 -m unittest test.py
# Calc
# Build a simple calculator with Flask, which uses URL query parameters to get the numbers to calculate with.

# Make a Flask app that responds to 4 different routes. Each route does a math operation with two numbers, a and b, which will be passed in as URL GET-style query parameters.

# /add
# Adds a and b and returns result as the body.
# /sub
# Same, subtracting b from a.
# /mult
# Same, multiplying a and b.
# /div
# Same, dividing a by b.
# For example, a URL like http://localhost:5000/add?a=10&b=20 should return a string response of exactly 30.

# Write the routes for this but don’t hardcode the math operation in your route function directly. Instead, we’ve provided helper functions for this in the file operations.py:

# calc/operations.py
# """Basic math operations."""

# def add(a, b):
#     """Add a and b."""
    
#     return a + b

# def sub(a, b):
#     """Substract b from a."""

#     return a - b

# def mult(a, b):
#     """Multiply a and b."""

#     return a * b

# def div(a, b):
#     """Divide a by b."""

#     return a / b
# Import and use these in your routes.

# After you’ve tried out your app, run the unit tests:

# $ python3 -m unittest test.py
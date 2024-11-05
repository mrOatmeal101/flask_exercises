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

# Section 5

# Section 6

# Section 7

# Section 8

# Section 9

# Section 10

# Section 11

# Section 12


#Import everything needed for program
from flask import Flask, redirect, render_template, request, url_for
import os

# Create the Flask instance
app = Flask(__name__)

# In case a typo is made in the code
app.config["DEBUG"] = True



# Create a route decorator
# This decorator is for the default login page
@app.route("/")
def index():
    if request.method == "GET":
        return render_template("login.html")


# This decorator is for the user main page
# The <name> will be the name of the person logged in at the moment
@app.route("/user/<name>")
def user_home(name):
    if request.method == "GET":
        return render_template("user_home.html", name=name)
    

# This decorator is for the create user account page
@app.route("/create_acct")
def create_acct():
    if request.method == "GET":
        return render_template("create_account.html")


# This decorator is for the invalid URL pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404_error.html"), 404
    

# This decorator is for the internal server error pages
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500_error.html"), 500
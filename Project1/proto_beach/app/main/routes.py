from flask import render_template
# import the blueprint class from the flask package the create a blueprint object
from app.main import bp


# Create a route using the bp object
# This is the welcome page index
@bp.route('/')
def index():
    return render_template('index.html')

# This is the login page route
@bp.route('/login/')
def login():
    return render_template('login.html')



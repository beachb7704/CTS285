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


# This is the register page route
@bp.route('/register/')
def register():
    return render_template('register.html')


# This is the change password page route
@bp.route('/change_password/')
def change_password():
    return render_template('change_password.html')


# This is the forgot password page route
@bp.route('/forgot_password/')
def forgot_password():
    return render_template('forgot_password.html')
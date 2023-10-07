#Import everything needed for program

from flask import Flask, redirect, render_template, request, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, InputRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from forms import *
from app import *


# Below is what is typed in when trying to create the database in the terminal window
#from app import app
#from app import db
# To run flask server
# python -m flask run


# Allows our app and login manager to work together and handles things when logging in
login_manager = LoginManager()
login_manager.session_protection = "strong"
#login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"


# Initialize the database
db = SQLAlchemy()

# To help hash the password
bcrypt = Bcrypt()


def create_app():
    # Create the Flask instance
    # Helps flask find all of the files in the directory
    app = Flask(__name__)

    # Add a database table. This will reference the table of the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataman.db'

    # Create a secret key to validate the form has not been tampered with
    app.config['SECRET_KEY'] = "secretkey"
    
    return app


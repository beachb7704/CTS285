# This is where I create my main blueprint for the application and render templates
from flask import Blueprint
bp = Blueprint('forms', __name__)
from app.main import routes
from config import Config

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SearchField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired



# Create a Form Class
class reg1ster(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired()])
    first_name = StringField("Enter your first name", validators=[DataRequired()])
    last_name = StringField("Enter your last name", validators=[DataRequired()])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Submit")
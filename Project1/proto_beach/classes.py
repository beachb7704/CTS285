from app import *
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime





#########
#CLASSES#
#########



# Create a Form Class
class create_account(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired()])
    first_name = StringField("Enter your first name", validators=[DataRequired()])
    last_name = StringField("Enter your last name", validators=[DataRequired()])
    password = StringField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Submit")
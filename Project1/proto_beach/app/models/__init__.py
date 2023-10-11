# This is where I create my main blueprint for the application and render templates
from flask import Blueprint
bp = Blueprint('models', __name__)
from app.main import routes
from app.extensions import db
from datetime import datetime
from config import Config
from flask_login import UserMixin

#################
# Student Table #
#################
# This creates the Flask-SQLAlchemy database model
class students(UserMixin,db.Model):
    username = db.Column(db.String(50), primary_key = True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    # The next line will create a relationship with a table not created yet
    answer_checker = db.relationship('Answer_Checker', backref='author', lazy=True)
    
    def __repr__(self):
        return f'<register "{self.username}">'


# This is an example for answer_checker. Can be changed depending on how we set this up.
class Answer_Checker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # This is creating the foreign key that will connect to the first table created.
    user_id = db.Column(db.String(50), db.ForeignKey('students.username'), nullable = False)
    num1 = db.Column(db.Integer, nullable = False)
    operator = db.Column(db.String(1), nullable = False)
    num2 = db.Column(db.Integer, nullable = False)
    
    def __repr__(self):
        return f'<register "{self.user_id}">'
# This is where I create my main blueprint for the application and render templates
from flask import Blueprint
bp = Blueprint('models', __name__)
from app.main import routes
from app.extensions import db
from datetime import datetime
from config import Config

#################
# Student Table #
#################
# This creates the Flask-SQLAlchemy database model
class students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<register "{self.username}">'



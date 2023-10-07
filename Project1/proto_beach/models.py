from app import db
from flask_login import UserMixin
from datetime import datetime



# Create Model for adding users to database
class User(UserMixin, db.Model):
    __tablename__ = 'students'
    user_id = db.Column("user_id", db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<User %r>' % self.username
    
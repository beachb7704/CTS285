from app import db, login_manager
from flask_login import UserMixin


# Creating a user loader for the login manager to work
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


##############
# User model #
##############

# Here we are going to create the model for the students table in the database.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    firstname = db.Column(db.String(20), nullable = False)
    lastname = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(20), nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
       
    def __repr__(self):
        return f"{self.username}"



############################
# student statistics model #
############################

# Here we are going to create the model for the students table in the database.
# This is an example for answer_checker. Can be changed depending on how we set this up.
class Student_Statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # This is creating the foreign key that will connect to the first table created.
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'), nullable = False)
    correct_questions = db.Column(db.Integer, nullable = False)
    wrong_questions = db.Column(db.Integer, nullable = False)
    total_questions = db.Column(db.Integer, nullable = False)
    
    def __repr__(self):
        return f'<register "{self.user_id}">'
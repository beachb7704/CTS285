import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Need to find a way to set it permanetly instead of setting it everytime I log in.
# To set the secret key, I had to type the following inside my visual studio code command prompt:
#   set SECRET_KEY="secretkey"

class Config:
    # This will keep the secret key private so nobody will be able to see it if they look at your code.
    # Secret key will need to be stated everytime visual studio code is closed out.
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'mathmaticus.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
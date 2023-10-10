import os

basedir = os.path.abspath(os.path.dirname(__file__))

# To set the secret key, I had to type the following inside my visual studio code command prompt:
#   set SECRET_KEY="secretkey"
# This will keep the secret key private so nobody will be able to see it if they look at your code.
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # These next two lines will be removed before going into production
    # Set the secret key to secretkey 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'mathmaticus.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
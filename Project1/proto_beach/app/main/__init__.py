# This is where I create my main blueprint for the application and render templates
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes
from config import Config
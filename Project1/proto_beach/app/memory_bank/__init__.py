from flask import Blueprint

bp = Blueprint('memory_bank', __name__)

from app.memory_bank import routes
from config import Config


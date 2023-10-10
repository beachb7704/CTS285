from flask import Blueprint
bp = Blueprint('Answer Checker', __name__)
from app.answer_checker import routes
from config import Config
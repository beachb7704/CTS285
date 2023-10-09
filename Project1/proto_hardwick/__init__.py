from flask import Blueprint
from tabulate import tabulate
from Question_Class import Question
from Answer_Checker import Answer_Checker
from UI_Class import UI
bp = Blueprint('main', __name__)
from app.answer_checker import routes
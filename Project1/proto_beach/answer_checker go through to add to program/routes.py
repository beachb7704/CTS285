from flask import render_template
from app.answer_checker import bp


@bp.route('/')
def index():
    return render_template('answer_checker/index.html')
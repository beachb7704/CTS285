from flask import render_template
from app.memory_bank import bp

@bp.route('/')
def index():
    return render_template('memory_bank/index.html')

@bp.route('/categories/')
def categories():
    return render_template('memory_bank/categories.html')
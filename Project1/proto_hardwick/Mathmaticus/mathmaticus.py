# flask --app M2HW2.py run --debug
# member variable object in app with there own routes
# url_for() and url redirect to connect brenda's front end to my back end
# url_for('veiwname', _external=True)
# use user session as storage for variables

# add tags for different types of questions (add, sub, multi, divide)

# move repeated code to a separate file
# figure out how to only show the equations for a specific user instead of all of the users.

# flash cards
# set up so that can ask one question at a time.
# learn session and login from:  https://flask.palletsprojects.com/en/3.0.x/tutorial/views/
# 

# General
# convert to sqlalchemy and wtforms
# https://www.digitalocean.com/community/tutorials/how-to-query-tables-and-paginate-data-in-flask-sqlalchemy

# freeze venv modules
# pip freeze -l > requirements.txt
# pip freeze --user > requirements.txt

import os
# import datetime
import sqlite3
import json
from flask import Flask, render_template, request, url_for, flash, redirect, Blueprint, g, session
from werkzeug.exceptions import abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, func
from Answer_Checker import Answer_Checker
from Question_Class import Question

# This is used with SQLAlchemy which I have not finished integrating yet
basedir = os.path.abspath(os.path.dirname(__file__))


def get_mem_bank_conn():
    """This function initializes the memory_bank.db database."""
    conn = sqlite3.connect('memory_bank.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_flash_cards_conn():
    """This function initializes the flash_cards.db database."""
    conn = sqlite3.connect('flash_cards.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_eqnset(user_id):
    """This function retrieves all of the equations from the memory bank for a given user"""
    conn = get_mem_bank_conn()
    eqnset = conn.execute('SELECT * FROM memory_bank WHERE user_id = ?',(user_id,)).fetchall()
    conn.close()
    if eqnset is None:
        abort(404)
    return eqnset

def get_eqn(user_id, row_id):
    """This function retrieves a specific user equation to be used by delete()."""
    conn = get_mem_bank_conn()
    eqn = conn.execute('SELECT * FROM memory_bank WHERE user_id = ? AND row_id = ?',(user_id, row_id)).fetchone()
    if eqn is None:
        abort(404)
    return eqn

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# implementing SQLAlchemy (not finished)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'flash_cards_alchemy.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

flash_cards_alchemy = SQLAlchemy(app)

class FlashCards(flash_cards_alchemy.Model):
    row_id = flash_cards_alchemy.Column(flash_cards_alchemy.Integer, primary_key=True)
    created = flash_cards_alchemy.Column(DateTime(timezone=True), server_default=func.now())
    #created_date = Column(DateTime, default=datetime.datetime.utcnow)
    category = flash_cards_alchemy.Column(flash_cards_alchemy.String(100), nullable=False)
    num1 = flash_cards_alchemy.Column(flash_cards_alchemy.Integer, nullable=False)
    operator = flash_cards_alchemy.Column(flash_cards_alchemy.String(1), unique=True, nullable=False)
    num2 = flash_cards_alchemy.Column(flash_cards_alchemy.Integer, nullable=False)
    ans = flash_cards_alchemy.Column(flash_cards_alchemy.Integer, nullable=False)

    def __repr__(self):
        return f'<Equation ({self.category}): {self.num1}{self.operator}{self.num2}={self.ans}>'

@app.route('/')
def index():
    return render_template('index.html')

# this allows me to set the user_id without having to login
# will be done by login later
# until I get this streamlined => add link to main page to remind me to set user at start
# print user id to landing page
@app.route('/setuser/<user_id>')
def setuser(user_id: str) -> str:
    session['user_id'] = user_id
    return 'User value set to: ' + session['user_id']

# this displays the user_id
@app.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user_id']

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/<user_id>')
def get_user_id(user_id):
    eqn_set = get_eqnset(user_id)
    return render_template('mem_bank.html', eqn_set=eqn_set, user_id=user_id)

@app.route('/<user_id>/<int:row_id>')
def get_user_eqn(user_id, row_id):
    eqn = get_eqn(user_id, row_id)
    return render_template('single_eqn.html', eqn=eqn, user_id=user_id)
    
# previously called create.html
@app.route('/answer_checker', methods=('GET', 'POST'))
def answer_checker():
    if request.method == 'POST':
        num1 = request.form['num1']
        math_op = request.form['math_op']
        num2 = request.form['num2']
        ans = request.form['ans']

        if not num1:
            flash('1st number is required!')
        elif not math_op:
            flash('The operator is required!')
        elif not num2:
            flash('2nd number is required!')
        elif not ans:
            flash('The answer is required!')
        elif not int(num1) and num1 != 0:
            flash('1st number is NOT an integer!')
        elif math_op != "+" and math_op != "-" and math_op != "*" and math_op != "/":
            flash('Please enter an appropriate operator!')
        elif not int(num2) and num2 != 0:
            flash('The 2nd number is NOT an integer!')
        # Mod to allow for negative ans
        elif not int(ans) and ans != 0:
            flash('The answer is NOT an integer!')
        else:
            true_or_false = Answer_Checker.right_or_wrong_var(num1,math_op,num2,int(ans))
            if true_or_false:
                eqn = num1 + " " + math_op + " " + num2 + " = " + ans 
            else:
                eqn = ""
            return render_template('answer_checker.html').format(feedback = true_or_false, eqn = eqn)

    return render_template('answer_checker.html').format(feedback="", eqn = "")

# Make sure to set the user_id before trying to use the Memory Bank
@app.route('/mem_bank')
def mem_bank():
    # AN: I think we can pull user_id out of session and then use it in the below query
    # something like user_id = session['user_id'] (see flaskr tutorial /views)
    
    eqn_set = get_eqnset(session['user_id'])
    return render_template('mem_bank.html', equations=eqn_set, user_id=session['user_id'])

@app.route('/mem_bank_add', methods=('GET', 'POST'))
def mem_bank_add():

    if request.method == 'POST':
        num1 = request.form['num1']
        math_op = request.form['math_op']
        num2 = request.form['num2']
        ans = request.form['ans']

        if not num1:
            flash('1st number is required!')
        elif not math_op:
            flash('The operator is required!')
        elif not num2:
            flash('2nd number is required!')
        elif not ans:
            flash('The answer is required!')
        elif not int(num1) and num1 != "0":
            flash('1st number is NOT an integer!')
        elif math_op != "+" and math_op != "-" and math_op != "*" and math_op != "/":
            flash('Please enter an appropriate operator!')
        elif not int(num2) and num2 != "0":
            flash('The 2nd number is NOT an integer!')
        elif not int(ans) and ans != "0":
            flash('The answer is NOT an integer!')
        else:
            true_or_false = Answer_Checker.right_or_wrong_var(num1,math_op,num2,int(ans))

            if true_or_false:
                # add get_user_id to import the user_id
                conn = get_mem_bank_conn()
                conn.execute("INSERT INTO memory_bank (user_id, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
                             (1, int(num1), math_op, int(num2), int(ans)))
                conn.commit()
                conn.close()
                eqn = num1 + " " + math_op + " " + num2 + " = " + ans 
            else:
                eqn = ""
            
            return render_template('mem_bank_add.html').format(feedback = true_or_false, eqn = eqn)

    return render_template('mem_bank_add.html').format(feedback="", eqn = "", equations = "")

# store variable in session

@app.route('/flash_cards', methods = ['GET','POST'])
def flash_cards():

    conn = get_flash_cards_conn()
    categories = conn.execute('SELECT DISTINCT category FROM flash_cards').fetchall()
    conn.close()

    if request.method == 'POST':
        
        cat_name = request.form['flash_card_set']
        session['cat_name'] = cat_name
        conn = get_flash_cards_conn()
        eqn_set = conn.execute('SELECT * FROM flash_cards WHERE category = ?',(cat_name,)).fetchall()
        conn.close()
        
        # TypeError: Object of type Row is not JSON serializable
        # session['eqn_set'] = eqn_set

        #ans = request.form['ans']
        
        # https://docs.python.org/3/library/json.html
        # json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
        # json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

        # for i in range(len(eqn_set)):
        for i in range(1):
            eqn = eqn_set[i]
            # add from_row to question class  
            #session['eqn'] = json.dumps({"num1": eqn[3], "math_op": eqn[4], "num2": eqn[5], "ans": eqn[6]})
            # we're now having the question class init from a row, then dumping it as json
            print("\n flash cards")
            eqn_q = Question(eqn)
            print(eqn_q)
            print("eqn dictionary internals are = ", eqn_q.__dict__)
            session['eqn'] = json.dumps(eqn_q.__dict__)
                  
            # print(quest)
            # eqn type:  <class 'sqlite3.Row'>
            # print("eqn type: ",type(eqn))
            # eqn[3] type:  <class 'int'>
            # eqn[4] type:  <class 'str'>
            # print("eqn[4] type: ", type(eqn[4]))
            # quest type:  <class 'Question_Class.Question'>
            # print("quest type: ",type(quest))
            # session['quest'] = quest
            # session['num1'] = eqn[3]
            # session['operator'] = eqn[4]
            # session['num2'] = eqn[5]
            # session['ans'] = eqn[6]
            # session['eqn'] = [eqn[3], eqn[4], eqn[5], eqn[6]]
            # print(str(session['num1']) + session['operator'] + str(session['num2']) + "=" + str(session['ans']))
            # print(str(session['eqn'][0]) + session['eqn'][1] + str(session['eqn'][2]) + "=" + str(session['eqn'][3]))
            # print(str(quest.num1) + quest.operator + str(quest.num2) + "=" + str(quest.ans))
            
            # print(session['quest'])
            # print("\n session['eqn']",session['eqn'])
            # print(type(session['eqn']))
            # temp_eqn = json.loads(session['eqn'])
            # print("\n temp_eqn(json.loads)",temp_eqn)
            # print(type(temp_eqn))
            # TypeError: Object of type Row is not JSON serializable
            # This error was occurring until I added the "[1]" to eqn to make eqn[1]
            # The session variables cannot store non JSON serializable data like is stored
            #   in the database. Therefore, must convert to understandable data before 
            #   storing in the session variables.
            # session['eqn'] = eqn
            # print(session['eqn'])
            
            #flash_card_set(cat_name, eqn)
            #return render_template('flash_cards.html', categories=categories, chosen_cat=cat_name, eqn=eqn)
            # return render_template('flash_card_set.html', categories=categories, chosen_cat=cat_name, eqn=eqn)
            return redirect(url_for('flash_card_set'))
            # return redirect(request.url)
            # return redirect(request.referrer)

    return render_template('flash_cards.html', categories=categories, chosen_cat="", eqn="")

# @app.route('/flash_card_set', methods = ['GET','POST'])
@app.route('/flash_card_set', methods = ['GET','POST'])
def flash_card_set():
    
    print('\n flash_card_set:')
    eqn = json.loads(session['eqn'])
    print('type(eqn): ', type(eqn))
    print("eqn = ", eqn)
    print(str(eqn['num1']) + eqn['operator'] + str(eqn['num2']) + "=" + str(eqn['ans']))
    print(session['cat_name'])
    
    if request.method == 'POST':
        ans = request.form['ans']
        
        true_or_false = Answer_Checker.right_or_wrong_var(eqn['num1'], eqn['operator'], eqn['num2'], eqn['ans'])
        if not true_or_false:
            eqn = ""
              
        return render_template('flash_card_set.html', chosen_name=session['cat_name'], eqn=eqn, ans=ans, T_F=true_or_false)
        # return render_template('flash_card_set.html', chosen_name="", eqn=eqn, ans="")
        # return redirect(url_for('flash_card_set'))
        # return redirect(url_for('flash_cards'))
        
    return render_template('flash_card_set.html', chosen_name=session['cat_name'], eqn=eqn, ans="", T_F="")


@app.route('/<int:user_id>/<int:row_id>/delete', methods=('POST',))
def delete(user_id, row_id):
    conn = get_mem_bank_conn()

    cursor_obj = conn.cursor()
    eqn = cursor_obj.execute('SELECT * FROM memory_bank WHERE user_id = ? AND row_id = ?',(user_id, row_id)).fetchone()
    eqn_str = str(eqn[3]) + eqn[4] + str(eqn[5]) + "=" + str(eqn[6])
    
    conn.execute('DELETE FROM memory_bank WHERE user_id = ? AND row_id = ?', (user_id, row_id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(eqn_str))
    return redirect(url_for('mem_bank'))

@app.route('/<int:row_id>/delete', methods=('POST',))
def delete_flash_cards(row_id):
    conn = get_flash_cards_conn()

    cursor_obj = conn.cursor()
    eqn = cursor_obj.execute('SELECT * FROM flash_cards WHERE row_id = ?',(row_id,)).fetchone()
    eqn_str = str(eqn[3]) + eqn[4] + str(eqn[5]) + "=" + str(eqn[6])
    
    conn.execute('DELETE FROM memory_bank WHERE user_id = ? AND row_id = ?', (user_id, row_id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(eqn_str))
    return redirect(url_for('flash_cards'))
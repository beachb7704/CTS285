# flask --app M2HW2.py run --debug
# db browser for sqlite
# member variable object in app with there own routes
# url_for() and url redirect to connect brenda's front end to my back end
# url_for('veiwname', _external=True)
# redirect to mem_bank.html and see if it saves the eqn in print
# use user session as storage for variables

# add tags for different types of questions (add, sub, multi, divide)

# fix answer_checker and memory bank to allow for neg numbs
# figure out how to increment equation num in memory bank
# figure out how to only show the equations for a specific user instead of all of the users.

# flash cards
# need user to use a drop-down menu to select the category of flash cards


import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from Answer_Checker import Answer_Checker

def get_db_connection():
    conn = sqlite3.connect('memory_bank.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_eqnset(user_id):
    conn = get_db_connection()
    eqnset = conn.execute('SELECT * FROM memory_bank WHERE user_id = ?',(user_id,)).fetchall()
    conn.close()
    if eqnset is None:
        abort(404)
    return eqnset

def get_eqn(user_id, row_id):
    conn = get_db_connection()
    eqn = conn.execute('SELECT * FROM memory_bank WHERE user_id = ? AND row_id = ?',(user_id, row_id)).fetchone()
    if eqn is None:
        abort(404)
    return eqn

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/<int:user_id>')
def get_user_id(user_id):
    eqn_set = get_eqnset(user_id)
    return render_template('display_eqns.html', eqn_set=eqn_set, user_id=user_id)

@app.route('/<int:user_id>/<int:row_id>')
def get_user_eqn(user_id, row_id):
    eqn = get_eqn(user_id, row_id)
    return render_template('single_eqn.html', eqn=eqn, user_id=user_id)
    
# previously called create.html
# Answer checker is not capable for handling negative answers:  need to fix
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
        elif not num1.isdigit():
            flash('1st number is NOT an integer!')
        elif math_op != "+" and math_op != "-" and math_op != "*" and math_op != "/":
            flash('Please enter an appropriate operator!')
        elif not num2.isdigit():
            flash('The 2nd number is NOT an integer!')
        # Mod to allow for negative ans
        elif not ans.isdigit():
            flash('The answer is NOT an integer!')
        else:
            true_or_false = Answer_Checker.right_or_wrong_var(num1,math_op,num2,int(ans))
            if true_or_false:
                eqn = num1 + " " + math_op + " " + num2 + " = " + ans 
            else:
                eqn = ""
            return render_template('answer_checker.html').format(feedback = true_or_false, eqn = eqn)

    return render_template('answer_checker.html').format(feedback="", eqn = "")

@app.route('/mem_bank')
def mem_bank():
    conn = get_db_connection()
    eqn_db = conn.execute('SELECT * FROM memory_bank').fetchall()
    conn.close()
    return render_template('mem_bank.html', equations=eqn_db)

# attempt at only displaying the equations for a specific user
#@app.route('/<int:user_id>/mem_bank')
#def mem_bank(user_id):

    #eqn_set = get_user_id(user_id)
#    return render_template('mem_bank.html', equations=eqn_db)

@app.route('/mem_bank_add', methods=('GET', 'POST'))
def mem_bank_add():

    conn = get_db_connection()
    eqn_db = conn.execute('SELECT * FROM memory_bank').fetchall()
    conn.commit()
    conn.close()

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
        elif not num1.isdigit():
            flash('1st number is NOT an integer!')
        elif math_op != "+" and math_op != "-" and math_op != "*" and math_op != "/":
            flash('Please enter an appropriate operator!')
        elif not num2.isdigit():
            flash('The 2nd number is NOT an integer!')
        elif not ans.isdigit():
            flash('The answer is NOT an integer!')
        else:
            true_or_false = Answer_Checker.right_or_wrong_var(num1,math_op,num2,int(ans))

            if true_or_false:
                # add get_user_id to import the user_id
                conn = get_db_connection()
                conn.execute("INSERT INTO memory_bank (user_id, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
                             (1, int(num1), math_op, int(num2), int(ans)))
                conn.commit()
                conn.close()
            else:
                eqn = ""
            
            return render_template('mem_bank_add.html').format(feedback = true_or_false, eqn = eqn, equations = eqn_db)

    return render_template('mem_bank_add.html').format(feedback="", eqn = "", equations = eqn_db)

# need to be able to remove a single equation from the database
@app.route('/<int:user_id>/<int:row_id>/delete', methods=('POST',))
def delete(user_id, row_id):
    conn = get_db_connection()

    cursor_obj = conn.cursor()
    eqn = cursor_obj.execute('SELECT * FROM memory_bank WHERE user_id = ? AND row_id = ?',(user_id, row_id)).fetchone()
    eqn_str = str(eqn[3]) + eqn[4] + str(eqn[5]) + "=" + str(eqn[6])
    
    conn.execute('DELETE FROM memory_bank WHERE user_id = ? AND row_id = ?', (user_id, row_id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(eqn_str))
    return redirect(url_for('mem_bank'))
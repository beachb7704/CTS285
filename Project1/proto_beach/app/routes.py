# Importing flask
import os
from flask import Flask, render_template, url_for, flash, redirect, request
from app.forms import Registration, Login, UpdateAccount
from app.models import User, Student_Statistics
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import secrets
from PIL import Image
from Answer_Checker import Answer_Checker



# Routes are what we create to move to other webpages.

#####################
# Home / Root Route #
#####################

# This is a default webpage route for our root or welcome page.
# The render_template returns our home.html webpage.
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


#############################
# Account Information Route #
#############################
# This will save the picture the user uploads with a random hex number
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
    # This will resize the picture to make it 125 X 125 in size
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn
    
# The render_template returns our accountinfo.html webpage.
@app.route("/accountinfo", methods = ['GET', 'POST'])
@login_required
def accountinfo():
    form = UpdateAccount()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.firstname = form.first_name.data
        current_user.lastname = form.last_name.data
        db.session.commit()
        flash("Your account has been successfully updated", 'success')
        return redirect(url_for('accountinfo'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.first_name.data = current_user.firstname
        form.last_name.data = current_user.lastname
    image_file = url_for('static', filename = 'images/' + current_user.image_file)
    return render_template('accountinfo.html', title = 'Account Info', image_file = image_file, form = form)


######################
# Registration Route #
######################
# This is creating the route for the registratin page to link the registration form
@app.route("/registration", methods = ['GET', 'POST'])
def registration():
    # This will check to see if current user is logged in and redirect them back to the welcome page if Register link is clicked
    #if current_user.is_authenticated:
    #    return redirect(url_for('home'))
    form = Registration()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, firstname=form.first_name.data, lastname=form.last_name.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'The account has been added successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html', title = 'Registration', form = form)




###############
# Login Route #
###############
# This is creating the route for the registratin page to link the registration form
@app.route("/login", methods = ['GET', 'POST'])
def login():
    # This will check to see if current user is logged in and redirect them back to the welcome page if Login link is clicked
    #if current_user.is_authenticated:
    #    return redirect(url_for('home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect (next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Either username or password was typed in incorrectly. Please try agian.")
    return render_template('login.html', title = 'Login', form = form)



################
# Logout Route #
################
# This is to log the user out of the current session so another user can log in. 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


########################
# Home Page Route #
########################
# This is to log the user out of the current session so another user can log in. 
@app.route("/game/checker")
@login_required
def checker():
    return render_template('checker.html', title='Answer Checker')



#########################
# Change Password Route #
#########################
# This is to log the user out of the current session so another user can log in. 
@app.route("/user_info/change_password")
def change_password():
    return render_template('change_password.html', title='Change Password')



###################
# check_ans Route #
###################
# This is to log the user out of the current session so another user can log in. 
@app.route("/check_ans", methods = ['GET','POST'])
@login_required
def check_ans():
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
            return render_template('checker.html').format(feedback = true_or_false, eqn = eqn)

    return render_template('checker.html').format(feedback="", eqn = "")


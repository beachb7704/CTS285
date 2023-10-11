from flask import render_template, request, url_for, redirect, flash
# import the blueprint class from the flask package the create a blueprint object
from app.main import bp
from app.models import students
from app.extensions import db, bcrypt
from config import Config
from app.auth import reg1ster
from app.auth import log1n



# Create a route using the bp object
# This is the welcome page index
@bp.route('/')
def index():
    return render_template('index.html')

# This is the login page route
@bp.route('/login/', methods = ('GET', 'POST'))
def login():
    
    # This will show the users in the database by the date added    
    #our_users = students.query.order_by(students.date_added)    
    return render_template('login.html')

@bp.route('/account_info/')
def account_info():
    return render_template('account_info.html')


# This is the register page route
@bp.route('/register/', methods=['GET', 'POST'])
def register():
    username = None
    first_name = None
    last_name = None
    password = None
    form = reg1ster()
    # Validate Form
    if form.validate_on_submit():
        # This will query the database to see if this username already exists
        user = students.query.filter_by(username=form.username.data).first()
        if user is None:
            # This will hash the password and save it to the database hashed
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            user= students(username=form.username.data, first_name=form.first_name.data, last_name=form.last_name.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            username = form.username.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            password = form.password.data    
            # This will clear the form out for the next submission
            form.username.data = ''
            form.first_name.data = ''
            form.last_name.data = ''
            form.password.data = ''
            flash("Account created!", 'success')
            return redirect(url_for('main.login'))                        
        else:
            username = form.username.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            password = form.password.data    
            # This will clear the form out for the next submission
            form.username.data = ''
            form.first_name.data = ''
            form.last_name.data = ''
            form.password.data = ''
            # This will put a flash banner across the screen if the form was submitted successfully.
            flash("This username already exists. Please try again.", 'warning')
        
    # This will show the users in the database by the date added    
    #our_users = students.query.order_by(students.date_added)    
    return render_template('register.html', form = form, username = username, first_name = first_name, last_name = last_name, password = password)


# This is the change password page route
@bp.route('/change_password/')
def change_password():
    return render_template('change_password.html')


# This is the forgot password page route
@bp.route('/forgot_password/')
def forgot_password():
    return render_template('forgot_password.html')


# This is the user home page route
@bp.route('/user_home/')
def user_home():
    return render_template('user_home.html')
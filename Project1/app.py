#Import everything needed for program
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



# Create the Flask instance
app = Flask(__name__)
# Create a secret key to validate the form has not been tampered with
app.config['SECRET_KEY'] = "secretkey"


##############
#FORM CLASSES#
##############

# Create a Form Class
class create_account(FlaskForm):
    first_name = StringField("Enter your first name", validators=[DataRequired()])
    last_name = StringField("Enter your last name", validators=[DataRequired()])
    username = StringField("Enter your username", validators=[DataRequired()])
    password = StringField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")



# Create a route decorator
# This decorator is for the default login page
@app.route("/")
def index():
    if request.method == "GET":
        return render_template("login.html")


# This decorator is for the user main page
# The <name> will be the name of the person logged in at the moment
@app.route("/user/<name>")
def user_home(name):
    if request.method == "GET":
        return render_template("user_home.html", name=name)
    

# This decorator is for the create user account page
# Want to set the variables the form asks to none since there is nothing yet provided by the user.
# Going to pull up the form from the class we created earlier.
@app.route("/add_acct", methods=['GET','POST'])
def create_acct():
    first_name = None
    last_name = None
    username = None
    password = None
    form = create_account()
    
    # Validate Form
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        password = form.password.data
        # This will clear the form out for the next submission
        form.first_name.data = ''
        form.last_name.data = ''
        form.username.data = ''
        form.password.data = ''
        # This will put a flash banner across the screen if the form was submitted successfully.
        flash("Account Created Successfully")
    
    return render_template("add_acct.html", first_name = first_name, last_name = last_name, username = username, password = password, form = form)




# This decorator is for the invalid URL pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404_error.html"), 404
    

# This decorator is for the internal server error pages
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500_error.html"), 500
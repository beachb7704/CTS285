from app import *
from models import *
from forms import *
from manage import *
from flask import Flask, render_template



# Used to reload the user object from the user id stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app = create_app()


# Create a route decorator
# This decorator is for the default login page
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("welcome.html", title="Welcome")

# Login route
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = login_Form()
        # Validate Form
        if form.validate_on_submit():
            # This will query the database to see if this username already exists
            user = User.query.filter_by(username=form.username.data).first()
            if user:
                if bcrypt.check_password_hash(user.password,form.password.data):
                    login_user(user)
                    return redirect(url_for("user_home"))
            else:
                flash("Username does not exist. Please try again.")
                return render_template("login.html", form=form)

        return render_template("login.html", form=form)


# Create a route decorator
# This decorator is for the default login page
@app.route("/user_home", methods=['GET', 'POST'])
#@login_required
def home():
    if request.method == "GET":
        return render_template("user_home.html")



# This decorator is for the user main page
# The <name> will be the name of the person logged in at the moment
@app.route("/top_scores")
def top_scores():
    if request.method == "GET":
        return render_template("top_scores.html")
    

# This decorator is for the create user account page
# Want to set the variables the form asks to none since there is nothing yet provided by the user.
# Going to pull up the form from the class we created earlier.
@app.route("/register", methods=['GET','POST'])
def register():
    username = None
    first_name = None
    last_name = None
    password = None
    form = registration_form()
    
    # Validate Form
    if form.validate_on_submit():
        # This will query the database to see if this username already exists
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            # This will hash the password and save it to the database hashed
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            user= User(username=form.username.data, first_name=form.first_name.data, last_name=form.last_name.data, password=hashed_password)
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
            # This will put a flash banner across the screen if the form was submitted successfully.
            flash("Account Created Successfully")
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
            flash("This username already exists")
        
    # This will show the users in the database by the date added    
    #our_users = students.query.order_by(students.date_added)    
    return render_template("register.html", form = form, username = username, first_name = first_name, last_name = last_name, password = password)







# Change the user password
@app.route("/change_password", methods=['GET','POST'])
def change_password():
    username = None
    password = None
    form = alter_password()
    
# This will show the users in the database by the date added    
    #our_users = students.query.order_by(students.date_added)    
    return render_template("change_password.html", form = form, username = username, password = password)


        


# This decorator is for the invalid URL pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404_error.html"), 404
    

# This decorator is for the internal server error pages
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500_error.html"), 500



if __name__ == "__main__":
    app.run(debug=True)

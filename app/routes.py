
from app import myapp, db, bcrypt
from models import User,Recipe
from app.forms import Registration,LoginForm
from flask import render_template,redirect,url_for,flash
from werkzeug.security import generate_password_hash
from flask_login import login_required
from app.models import User


@myapp.route('/')
def home():
    return "home page"

@myapp.route('/test')
def test():
    return "test123"

@myapp.route("/registration",methods=['GET','POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=generate_password_hash(form.password.data))
        db.session.add(new_user)
        db.session.commit()
        flash('successful', 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', form=form)

@myapp.route("/home/recipe")
@login_required
def view_recipe():
    recipes = Recipe.query.all()
    return render_template("recipe.html", recipes=recipes)
# log in
@myapp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm
    if form.validate_on_submit():
        # to check if the email entered in the form == the email in the db
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): # check if the user exist in the db
                                                                                   # and if the entered password is matched with the hash_password in the db
            #login_user(user)
            flash('Login successful!', 'success')                                                                   
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please check your email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


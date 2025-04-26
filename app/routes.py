from app import myapp, db, bcrypt
from app.forms import LoginForm
from app.models import User
from flask import render_template, redirect, url_for, flash

@myapp.route('/')
def home():
    return "home page"

@myapp.route('/test')
def test():
    return "test123"

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
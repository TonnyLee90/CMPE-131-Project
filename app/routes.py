from app import myapp
from app import db
from models import User,Recipe
from app.forms import Registration
from flask import render_template,redirect,url_for,flash
from werkzeug.security import generate_password_hash
from flask_login import login_required



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

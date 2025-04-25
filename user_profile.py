from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from models import Recipe

user_profile = Blueprint('user_profile', __name__)

@user_profile.route('/profile')
@login_required
def profile():
    user = current_user
    recipes = Recipe.query.filter_by(user_id=user.id).all()
    return render_template('profile.html', user=user, recipes=recipes)


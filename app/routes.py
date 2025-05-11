from app import myapp, db, bcrypt
from app.forms import LoginForm, RegistrationForm, RecipeForm, CommentForm, RatingForm, BookmarkForm, SearchForm
from app.models import User, Recipe, Comment, Rating
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, current_user, logout_user

# 0. Home page + 14. View All Recipes (Tonny)
@myapp.route('/')
@myapp.route('/home')
def home():
    recipes = Recipe.query.all() # search all recipes from the db
    bookmark_form=BookmarkForm()
    return render_template('home.html', recipes=recipes, bookmark_form=bookmark_form)

# 1. Registration (Sergio)
@myapp.route("/registration",methods=['GET','POST'])
def register():
    # when login user trys to access this page, then redirect them back to home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        # Check if username already exists
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('home'))
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #to encryt the password to hashed_password
        new_user = User(email=form.email.data, username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return redirect(url_for('home'))

# 2. Login (Tonny)
@myapp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # to check if the email entered in the form == the email in the db
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): # check if the user exist in the db
                                                                                   # and if the entered password is matched with the hash_password in the db
            login_user(user)
            flash('Loged in successful!', 'success')                                                                   
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please check your email and password.', 'danger')
    return redirect(url_for('home'))

# 3. Logout (Sergio)
@myapp.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

# 4. Create a new recipe (Tonny)
@myapp.route('/recipe/new', methods=['GET', 'POST'])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        # add the recipe data to the db
        recipe = Recipe(title=form.title.data, description=form.description.data,
                        ingredients=form.ingredients.data, instructions=form.instructions.data,
                        author=current_user)
        # Save the data entered in the form to the db
        db.session.add(recipe)
        db.session.commit()

        flash('Recipe added successfully!')
        return redirect(url_for('home'))
    
    return render_template('new_recipe.html', form=form)
# 5. Edit a recipe

# 6. Delete a recipe (Tonny)
@myapp.route('/recipe/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id) # Search a recipe by id, if it's not found, return error 404
    if recipe.author != current_user: # Check if the recipe's user != current_user
        flash('You do not have permission to delete')
        return redirect(url_for('home'))
    
    # delete the post
    db.session.delete(recipe)
    db.session.commit()

    flash('Recipe deleted!')

    return redirect(url_for('home'))

# 7. Show a detailed recipe + 10. Common a recipe (Tonny)
# ex: when user clicked /recipe/35 -> Flask sees <int:recipe_id> in the route ->  recipe_id = 42 in this function"
@myapp.route('/recipe/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id) # Search a recipe by id, if it's not found, return error 404
    form = CommentForm()
    # if save_form.submit.data and save_form.validate_on_submit():
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, recipe=recipe, user=current_user)
        db.session.add(comment)
        db.session.commit()
        flash('Comment added!', 'success')
        return redirect(url_for('recipe', recipe_id = recipe.id))
    
    return render_template('view_recipe.html', recipe=recipe, form=form)

# 8. Search a recipe (William)
@myapp.route('/search', methods=['GET'])
def search():
    form = SearchForm()
    results = None
    if form.validate():
        keyword = form.keyword.data
        results = Recipe.query.filter(title=keyword).all() # use ilike for partial matching

    return render_template('index.html', form=form, results=results)

# 9. Rate a recipe (Tonny)
@myapp.route('/recipe/<int:recipe_id>/rate', methods=['GET', 'POST'])
@login_required
def rate_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    form = RatingForm()

    # Check if the user already rated this recipe
    existing_rating = Rating.query.filter_by(user_id=current_user.id, recipe_id=recipe.id).first()

    if form.validate_on_submit():
            rating = Rating(star=form.stars.data, user=current_user, recipe=recipe) # add new rating to the db
            db.session.add(rating)
            db.session.commit()
            flash('Your rating has been added.', 'success')
    return redirect(url_for('view_recipe', recipe_id=recipe.id))

# 10. Common a recipe (in reciple route)

# 11. view User profile
@myapp.route('/profile')
#@login_required
def profile():
    return render_template('profile.html', user=current_user)

# 12. Edit User profile

# 13. Save or Unsave Recipe (Favorites) # Tonny
@myapp.route('/recipes/<int:recipe_id>/save', methods=['POST'])
@login_required
def save_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    # if the recipe is already in the Favorites, then unsave the recipe
    if recipe in current_user.favorites:
        current_user.favorites.remove(recipe)
        flash('Recipe removed from favorites.')
    else:
        # Otherwise, save the recipe to the Favorites
        # don't use db.session.add(recipe) again because the recipe already exists in the database:
        # just trying to associate it with a user
        current_user.favorites.append(recipe)
        flash('Recipe saved to favorites.')
    db.session.commit()
    return redirect(request.referrer or url_for('home'))

# 14. View all recipes,  code is in route for the home page (Tonny)

# 15. Filter Recipes

# 16. View all recipes posted by current user (Tonny)
@myapp.route('/my-recipes')
@login_required
def my_recipes():
    recipes = Recipe.query.filter_by(author=current_user).all()
    return render_template('my_recipes.html', recipes=recipes)

# 17. View all saved recipes (Tonny)
@myapp.route('/favorites')
@login_required
def view_saved_recipes():
    saved_recipes = current_user.favorites  # aceess many-to-many table
    return render_template('favorites_recipes.html', recipes=saved_recipes)
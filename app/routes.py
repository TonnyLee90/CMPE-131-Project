from app import myapp, db, bcrypt
from app.forms import LoginForm, RegistrationForm, RecipeForm, CommentForm, RatingForm, EditProfileForm, BookmarkForm, SearchForm
from app.models import User, Recipe, Comment, Rating
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, current_user, logout_user

# 0. Home page + 14. View All Recipes (Tonny)
@myapp.route('/')
@myapp.route('/home')
def home():
    recipes = Recipe.query.all() # search all recipes from the db
    bookmark_form = BookmarkForm()
    search_form = SearchForm()
    return render_template('home.html', recipes=recipes, bookmark_form=bookmark_form, search_form=search_form)

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

# 4. Create a new recipe (Sergio)
@myapp.route('/recipe/new', methods=['GET', 'POST'])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        # add the recipe data to the db
        recipe = Recipe(title=form.title.data, description=form.description.data,
                        ingredients=form.ingredients.data, instructions=form.instructions.data,
                        author=current_user, tags=form.tags.data)
        # Save the data entered in the form to the db
        db.session.add(recipe)
        db.session.commit()

        flash('Recipe added successfully!')
        return redirect(url_for('home'))
    
    return render_template('new_recipe.html', form=form)

# 5. Edit a recipe (Sergio)
@myapp.route('/edit_recipe/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    # Only allow the author to edit
    if recipe.author != current_user:
        flash("You are not authorized to edit this recipe.", "danger")
        return redirect(url_for('my_recipes'))
    
    form = RecipeForm(obj=recipe)  # prefill with existing data

    if form.validate_on_submit():
        recipe.title=form.title.data
        recipe.description=form.description.data
        recipe.ingredients=form.ingredients.data
        recipe.instructions=form.instructions.data

        db.session.commit()

        flash("Recipe updated successfully!", "success")
        return redirect(url_for('recipe', recipe_id=recipe.id))

    return render_template('edit_recipe.html', form=form, recipe=recipe)

# 6. Delete a recipe (Tonny)
@myapp.route('/edit_recipe/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id) # Search a recipe by id, if it's not found, return error 404
    if recipe.author != current_user: # Check if the recipe's user != current_user
        flash('You do not have permission to delete', 'danger')
        return redirect(url_for('home'))
    
    # delete the post
    db.session.delete(recipe)
    db.session.commit()

    flash('Recipe deleted!', 'success')

    return redirect(url_for('home'))

# 7. Show a detailed recipe + 10. Common a recipe (Sergio, Tonny)
# ex: when user clicked /recipe/35 -> Flask sees <int:recipe_id> in the route ->  recipe_id = 42 in this function"
@myapp.route('/recipe/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id) # Search a recipe by id, if it's not found, return error 404
    form = CommentForm()
    rating_form=RatingForm()
    # if save_form.submit.data and save_form.validate_on_submit():
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, recipe=recipe, user=current_user)
        db.session.add(comment)
        db.session.commit()
        flash('Comment added!', 'success')
        return redirect(url_for('recipe', recipe_id = recipe.id))
    
    return render_template('view_recipe.html', recipe=recipe, form=form, rating_form=rating_form)

# 8. Rate a recipe (Tonny)
@myapp.route('/recipe/<int:recipe_id>/rate', methods=['GET', 'POST'])
@login_required
def rate_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    form = RatingForm()

    if form.validate_on_submit():
            rating = Rating(stars=form.stars.data, user=current_user, recipe=recipe) # add new rating to the db
            db.session.add(rating)
            db.session.commit()
            flash('Your rating has been added.', 'success')
    return redirect(url_for('recipe', recipe_id=recipe.id))

# 9. Search a recipe with filter (Tonny + William)
@myapp.route('/search', methods=['GET', 'POST'])
def search():
    search_form = SearchForm()
    bookmark_form = BookmarkForm()
    # set is used to store unique elements (tag)
    tag_set = set()
    # All tages from the recipes in the db
    all_recipes = Recipe.query.with_entities(Recipe.tags).all() # with_entities() returns tuples, ex: [('dessert,quick',), ('vegan',), (None,), ('healthy',)]
    #search_form.tag.choices = [('', 'All Tags')] + [(tag, tag.capitalize()) for tag in tag_set]
    
    for recipe_tags, in all_recipes:  # unpack tuple ('dessert,quick',)
        if recipe_tags:
            # Convert all tags to lowercase
            lowercase_tags = recipe_tags.lower()
            # Split the string into a list of individual tags (e.g., "vegan, quick" -> ["vegan", " quick"])
            tag_list = lowercase_tags.split(',')
            #  Add all tags into the set
            tag_set.update(tag_list)

    search_form.tag.choices = [('', 'All Tags')] + [(tag, tag.capitalize()) for tag in tag_set]
    
    # start with a base search
    recipes = Recipe.query
    if search_form.validate_on_submit():
        keyword = search_form.keyword.data
        tag = search_form.tag.data

    # filter by keyword first
    if keyword:
        recipes = recipes.filter(
            Recipe.title.ilike(f'%{keyword}%') | Recipe.description.ilike(f'%{keyword}%')

        )
    # If a tag was selected
    if tag:
        recipes = recipes.filter(Recipe.tags.ilike(f'%{tag}%'))

    recipes = recipes.order_by(Recipe.created.desc()).all()
        
    return render_template('search_results.html', recipes=recipes, search_form=search_form, bookmark_form=bookmark_form)

# 10. Common a recipe, code is in reciple route (Tonny)

# 11. view User profile (William)
@myapp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

# 12. Edit User profile (Tonny, William)
@myapp.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(obj=current_user)  # pre-fill with current data
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data

        # only update if password was entered
        if form.password.data:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            current_user.password=hashed_password

        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('profile'))

    return render_template('edit_profile.html', form=form)

# 13. Save or Unsave Recipe (Favorites) # Tonny
@myapp.route('/recipes/<int:recipe_id>/save', methods=['POST'])
@login_required
def save_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    # if the recipe is already in the Favorites, then unsave the recipe
    if recipe in current_user.favorites:
        current_user.favorites.remove(recipe)
        flash('Recipe removed from favorites.', 'info')
    else:
        # Otherwise, save the recipe to the Favorites
        # don't use db.session.add(recipe) again because the recipe already exists in the database:
        # just trying to associate it with a user
        current_user.favorites.append(recipe)
        flash('Recipe saved to favorites.', 'success')
    db.session.commit()
    return redirect(request.referrer or url_for('home'))

# 14. View all recipes,  code is in route for the home page (Tonny)

# 15. Filter Recipes, code is in the search route (Tonny and William)

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
from app import app
from app.forms import RecipeForm
@myapp.route('/')
def home():
    recipes = Recipe.query.all() # search all recipes from the db
    # return render_template('home.html', recipes=recipes)
    return render_template('home.html', recipes=recipes)

@myapp.route('/test')
def test():
    return "test123"

# This page is used to add a new recipe
@myapp_obj.route('/recipe/new', methods=['GET', 'POST'])
#@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(title=form.title.data, description=form.description.data,
                        ingredients=form.ingredients.data, instructions=form.instructions.data,
                        author=current_user)
        # Save the data entered in the form to the db
        db.session.add(recipe)
        db.session.commit()

        flash('Recipe added successfully!')
        return redirect(url_for('home'))
    
    return render_template('new_recipe.html', form=form)


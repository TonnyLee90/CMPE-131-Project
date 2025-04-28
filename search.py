from flask import Blueprint, request, render_template
from models import Recipe
from flask_login import login_required

search = Blueprint('search', __name__)

@search.route('/search', methods=['GET'])
@login_required
def search_recipes():
    query = request.args.get('q')
    if query:
        results = Recipe.query.filter(Recipe.title.contains(query) | Recipe.ingredients.contains(query)).all()
    else:
        results = []
    return render_template('search_results.html', recipes=results, query=query)


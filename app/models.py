from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

# To reload a user from the session.
# so Flask-Login knows who is logged in 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# to link two tables: User and Recipe
# Simple many-to-many, no extra fields	
favorites = db.Table(
    'favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(50), unique = True, nullable=False)
    # create a connection to the table 2
    recipes = db.relationship('Recipe', backref='author', lazy=True)

    # connection with the comments and ratings
    # A user can have more than one comments or ratings
    # back_populates:  Tells SQLAlchemy to link this with the user attribute in the Comment model. 
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete-orphan')
    ratings = db.relationship('Rating', back_populates='user', cascade='all, delete-orphan')
    # A user save many recipes, and each recipe can be saved by many users.
    
    favorites = db.relationship('Recipe', secondary=favorites, backref='favorited_by')
    
    def __repr__(self):
        return f"User('{self.username}')"

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    # for filter
    tags = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # connection with the comments and ratings
    # A user recipe can have more than one comments or ratings
    
    comments = db.relationship('Comment', back_populates='recipe', cascade='all, delete-orphan')
    ratings = db.relationship('Rating', back_populates='recipe', cascade='all, delete-orphan')
    
    def average_rating(self):
        toatal_ratings = 0
        # check if there's any existing rating
        if not self.ratings: # if 0 rating
            return None
        for rating in self.ratings:
            toatal_ratings += rating.stars
        return round((toatal_ratings/len(self.ratings)), 1)
        
    def __repr__(self):
        return f"Recipe('{self.title}', '{self.created}')"
"""
cascade='all, delete-orphan'
This tells SQLAlchemy what to do with related records when the parent (Recipe Post) is deleted:
If a User is deleted, all their comments are also deleted.
If a Recipe is deleted, all their comments are also deleted.
delete-orphan = also delete comments that no longer belong to a parent.
"""
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # to get the user who posted the comment (comment.user.username )
    recipe = db.relationship('Recipe', back_populates='comments')
    # get the recipe this comment belongs to (comment.recipe.title)
    # This Comment model is linked to a User, and that link should correspond to the comments relationship defined on the User model.
    user = db.relationship('User', back_populates='comments')

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, nullable=False)  # should be 1–5

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

    user = db.relationship('User', back_populates='ratings')
    recipe = db.relationship('Recipe', back_populates='ratings')
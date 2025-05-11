from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, HiddenField, TextAreaField, EmailField, validators

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[validators.InputRequired()])
    description = TextAreaField('Description', validators=[validators.InputRequired()])
    ingredients = TextAreaField('Ingredients', validators=[validators.InputRequired()])
    instructions = TextAreaField('Instructions', validators=[validators.InputRequired()])
    submit = SubmitField('Submit!')

'''Registration email/password'''
class RegistrationForm(FlaskForm):
    email = EmailField('Email', validators=[validators.InputRequired()])
    username = StringField("Username", validators=[validators.InputRequired()])
    password = PasswordField("Password", validators=[validators.InputRequired()])
    submit =  SubmitField("Sign Up!")

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[validators.InputRequired()])
    password = PasswordField('Password', validators=[validators.InputRequired()])
    submit =  SubmitField("Login")

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[validators.InputRequired(), validators.Length(min=1, max=500, message='add error msg here')])
    submit = SubmitField('Post Comment')

class RatingForm(FlaskForm):
    stars = IntegerField('Rating (1 to 5)', validators=[validators.InputRequired(), validators.NumberRange(min=1, max=5)])
    submit = SubmitField('Submit Rating')

class BookmarkForm(FlaskForm):
    submit = SubmitField('Bookmark')
    
class SearchForm(FlaskForm):
    keyword = StringField('What\' are you thinking', validators=[validators.InputRequired()])
    #category = StringField('Search by Category')
    submit = SubmitField('Search')
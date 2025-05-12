from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, HiddenField, RadioField, TextAreaField, EmailField, validators, SelectField

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[validators.InputRequired()])
    description = TextAreaField('Description', validators=[validators.InputRequired()])
    ingredients = TextAreaField('Ingredients', validators=[validators.InputRequired()])
    instructions = TextAreaField('Instructions', validators=[validators.InputRequired()])
    tags = StringField('Tags (comma-separated)', validators=[validators.Optional()])
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
    #stars = IntegerField('Rating (1 to 5)', validators=[validators.InputRequired(), validators.NumberRange(min=1, max=5)])
    stars = RadioField('Rating', choices=[('1', '1 ⭐'), ('2', '2 ⭐⭐'), ('3', '3 ⭐⭐⭐'), ('4', '4 ⭐⭐⭐⭐'), ('5', '5 ⭐⭐⭐⭐⭐')], validators=[validators.InputRequired()])
    submit = SubmitField('Rate')

class BookmarkForm(FlaskForm):
    submit = SubmitField('Bookmark')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[validators.Optional()])
    email = StringField('Email', validators=[validators.Optional()])
    password = PasswordField("Password", validators=[validators.Optional()])
    confirm_password = PasswordField('Confirm Password', validators=[validators.EqualTo('password', message='Passwords must match.'), validators.Optional()])
    submit = SubmitField('Update')

class SearchForm(FlaskForm):
    keyword = StringField('What\' are you thinking', validators=[validators.InputRequired()])
    # filter by
    tag = SelectField('Tag', choices=[], validators=[validators.Optional()])
    submit = SubmitField('Search')
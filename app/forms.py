from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, EmailField, validators


class LoginForm(FlaskForm):
    email = EmailField('Username', validators=[validators.InputRequired()])
    password = PasswordField('Password', validators=[validators.InputRequired()])
    submit =  SubmitField("Login")

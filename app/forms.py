from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, EmailField, validators
from wtforms.validators import DataRequired

'''Registration email/password '''
class Registration(FlaskForm):
    username=StringField("User name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = EmailField('Username', validators=[validators.InputRequired()])
    password = PasswordField('Password', validators=[validators.InputRequired()])
    submit =  SubmitField("Login")

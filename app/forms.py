from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

'''Registration email/password '''
class Registration(FlaskForm):
    username=StringField("User name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


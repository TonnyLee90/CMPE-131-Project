from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from app.forms import LoginForm, RegistrationForm, SearchForm
myapp = Flask(__name__)
# set up db location
myapp.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
myapp.config['SECRET_KEY'] = 'fjgrehfigubhfjlsdhgui56789094567845397y7uhy'
db = SQLAlchemy(myapp)
bcrypt = Bcrypt(myapp)
csrf = CSRFProtect(myapp) # for building the form manually; {{ form.hidden_tag() }}  using a Flask-WTF form object

# login
login_manager = LoginManager(myapp)
# Custom message to notify the user
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "info"
# Redirect URL for unauthorized access
login_manager.login_view = 'login'

# The following forms will be available in all templates
@myapp.context_processor
def inject_forms():
    return {
        'login_form': LoginForm(),
        'registration_form': RegistrationForm(),
        'search_form': SearchForm()
    }
from app import routes

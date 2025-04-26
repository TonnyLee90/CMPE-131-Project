from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager


# set up db location
login=LoginManager()
login.init_app(myapp)

from models import User
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

myapp = Flask(__name__)
# set up db location
myapp.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
myapp.config['SECRET_KEY'] = 'ULTRA-SECRET-DONT-SHARE'
db = SQLAlchemy(myapp)
from app import routes

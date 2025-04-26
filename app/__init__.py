from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

myapp = Flask(__name__)
# set up db location
myapp.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
myapp.config['SECRET_KEY'] = 'ULTRA-SECRET-DONT-SHARE'
db = SQLAlchemy(myapp)
login=LoginManager()
login.init_app(myapp)

from app import routes

from models import User
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


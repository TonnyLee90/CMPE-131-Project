from flask import Flask
from flask_sqlalchemy import SQLAlchemy

myapp = Flask(__name__)
# set up db location
myapp.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
db = SQLAlchemy(myapp)
from app import routes


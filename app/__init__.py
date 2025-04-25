from flask import Flask
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
=======

myapp = Flask(__name__)
# set up db location
myapp.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
db = SQLAlchemy(myapp)
from app import routes
>>>>>>> 97bd1ac1395a7e4f69b6d12be8c8aee7d3f52400

myapp = Flask(__name__)
# set up db location
myapp.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
db = SQLAlchemy(myapp)
from app import routes
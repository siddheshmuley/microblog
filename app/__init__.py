from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#this app is a variable
app = Flask(__name__)
#read from config file
app.config.from_object('config')

db = SQLAlchemy(app)
#this app is a package
from app import views, models
#script at the end to avoid circular reference because the views will reference the app variable defined here
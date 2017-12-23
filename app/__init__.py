from flask import Flask
#this app is a variable
app = Flask(__name__)
#this app is a package
from app import views
#script at the end to avoid circular reference because the views will reference the app variable defined here
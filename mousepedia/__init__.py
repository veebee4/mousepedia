# import modules and functions
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# checking if env.py file exists for environment settings
if os.path.exists("env.py"):
    import env

# creating flask application and app configuration files
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# assigning SQLAlchemy class instance to variable
db = SQLAlchemy(app)

from mousepedia import routes
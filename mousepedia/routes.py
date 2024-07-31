# import modules and functions
from flask import render_template, Flask
from mousepedia import app, db
from mousepedia.models import Park, Restaurant, Ride

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/parks")
def parks():
    return render_template("parks.html")
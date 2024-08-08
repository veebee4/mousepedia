# import modules and functions
from flask import render_template, session, request, redirect, url_for
from mousepedia import app, db
from mousepedia.models import Park, Restaurant, Ride


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/parks")
def parks():
        return render_template("parks.html", parks=parks)


@app.route("/add_park", methods=["GET", "POST"])
def add_park():
    if request.method == "POST":
        park = Park(park_name=request.form.get("park_name"))
        db.session.add(park)
        db.session.commit()
        return redirect(url_for("parks"))
    return render_template("add_park.html")
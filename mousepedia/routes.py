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
    print(f"Request method: {request.method}")  # Debug: Check the request method
    if request.method == "POST":
        park_name = request.form.get("park_name")
        print(f"Park name from form: {park_name}")  # Debug: Check the park name received
        if park_name:
            try:
                new_park = Park(park_name=park_name)
                db.session.add(new_park)
                db.session.commit()
                print("New park added and committed to the database")  # Debug: Confirm successful DB operation
                return redirect(url_for("parks"))
            except Exception as e:
                print(f"Error occurred: {e}")  # Debug: Print any errors during DB operations
                db.session.rollback()  # Rollback the session in case of error
        else:
            print("Park name is missing")  # Debug: Park name was not provided
    else:
        print("GET request received")  # Debug: Confirm that the GET request is handled
    return render_template("add_park.html")
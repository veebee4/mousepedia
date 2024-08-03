from mousepedia import db



class Restaurant(db.Model):
    #schema for the Restaurants model
    id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(50), unique=True, nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey("park.id"), nullable=False)
    restaurant_location = db.Column(db.Text, nullable=False)
    dine_or_quick_service = db.Column(db.Boolean, default=False, nullable=False)
    food_type = db.Column(db.String(30), nullable=False)
    restaurant_description = db.Column(db.Text, nullable=False)
    parks = db.relationship("Park", backref="restaurant", cascade="all, delete", lazy=True)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.restaurant_name



class Ride(db.Model):
    #schema for the Rides model
    id = db.Column(db.Integer, primary_key=True)
    ride_name = db.Column(db.String(50), unique=True, nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey("park.id", ondelete="CASCADE"), nullable=False)
    ride_location = db.Column(db.String(50), nullable=False)
    ride_description = db.Column(db.Text, nullable=False)
    parks = db.relationship("Park", backref="ride", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.ride_name



class Park(db.Model):
    #schema for the Parks model
    id = db.Column(db.Integer, primary_key=True)
    park_name = db.Column(db.String(50), unique=True, nullable=False)
    park_address = db.Column(db.String(50), unique=True, nullable=False)
    park_description = db.Column(db.Text, nullable=False)
    date_opened = db.Column(db.Date, nullable=False)
    time_open = db.Column(db.Time, nullable=False)
    time_closed = db.Column(db.Time, nullable=False)
    num_restaurants = db.Column(db.Integer, nullable=False)
    restaurant_ids = db.Column(db.Integer, db.ForeignKey("restaurant.id", ondelete="CASCADE"), nullable=False)
    num_rides = db.Column(db.Integer, nullable=False)
    ride_ids = db.Column(db.Integer, db.ForeignKey("ride.id", ondelete="CASCADE"), nullable=False)
    entertainment = db.Column(db.Text, nullable=False)
    special_features = db.Column(db.Text, nullable=False)
    transport_between_parks = db.Column(db.Text, nullable=False)
    restaurants = db.relationship("Restaurant", backref="park", cascade="all, delete", lazy=True)
    rides = db.relationship("Ride", backref="park", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.park_name
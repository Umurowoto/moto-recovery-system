from app import db
from datetime import datetime

class VehicleReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    vehicle_type = db.Column(db.String(20))  # motorbike | car
    plate_number = db.Column(db.String(30), index=True)
    chassis_number = db.Column(db.String(50), index=True)
    make = db.Column(db.String(50))

    complainant_name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    station_name = db.Column(db.String(100))

    county_id = db.Column(db.Integer, db.ForeignKey("county.id"))

    reported_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_recovered = db.Column(db.Boolean, default=False)

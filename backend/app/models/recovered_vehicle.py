from app import db
from datetime import datetime

class RecoveredVehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(30))
    chassis_number = db.Column(db.String(50))
    found_at = db.Column(db.DateTime, default=datetime.utcnow)

    station_id = db.Column(db.Integer, db.ForeignKey("police_station.id"))

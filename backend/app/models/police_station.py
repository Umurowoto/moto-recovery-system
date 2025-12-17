from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
fro

class PoliceStation(db.Model):
    __tablename__ = "police_stations"

    id = db.Column(db.Integer, primary_key=True)
    station_name = db.Column(db.String(100), nullable=False)
    station_code = db.Column(db.String(50), unique=True, nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey("counties.id"), nullable=False)

    phone_number = db.Column(db.String(20))
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    vehicle_reports = db.relationship("VehicleReport", backref="station", lazy=True)

    # Security
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "stationName": self.station_name,
            "stationCode": self.station_code,
            "county": self.county.name,
            "phoneNumber": self.phone_number,
            "createdAt": self.created_at.isoformat()
        }

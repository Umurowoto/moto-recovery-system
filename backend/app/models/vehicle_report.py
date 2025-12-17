from datetime import datetime, timedelta
from app import db

class VehicleReport(db.Model):
    __tablename__ = "vehicle_reports"

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    county_id = db.Column(db.Integer, db.ForeignKey("counties.id"), nullable=False)
    station_id = db.Column(db.Integer, db.ForeignKey("police_stations.id"), nullable=False)

    # Complainant
    complainant_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    # Vehicle details
    vehicle_type = db.Column(db.String(20), nullable=False)  # motorbike | car
    plate_number = db.Column(db.String(50), nullable=False, index=True)
    chassis_number = db.Column(db.String(100), nullable=False, index=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100))
    color = db.Column(db.String(50))

    reported_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_claimed = db.Column(db.Boolean, default=False)

    def is_unclaimed(self):
        return (
            not self.is_claimed and
            datetime.utcnow() >= self.reported_at + timedelta(days=180)
        )

    def to_dict(self):
        return {
            "id": self.id,
            "vehicleType": self.vehicle_type,
            "plateNumber": self.plate_number,
            "chassisNumber": self.chassis_number,
            "make": self.make,
            "model": self.model,
            "color": self.color,
            "complainantName": self.complainant_name,
            "phoneNumber": self.phone_number,
            "station": self.station.station_name,
            "county": self.county.name,
            "reportedAt": self.reported_at.isoformat(),
            "isClaimed": self.is_claimed,
            "isUnclaimed": self.is_unclaimed()
        }

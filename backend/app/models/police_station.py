from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class PoliceStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_name = db.Column(db.String(100), nullable=False)
    station_code = db.Column(db.String(50), unique=True, nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey("county.id"))
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

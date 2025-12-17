from flask import Flask
from flask_cors import CORS

from app.config import Config
from app.extensions import db, migrate, jwt

# Import models so migrations can see them
from app.models import County, PoliceStation, VehicleReport, Admin

# Import routes
from app.routes.admin_routes import admin_bp
from app.routes.police_routes import police_bp
from app.routes.report_routes import report_bp
from app.routes.recovered_routes import recovered_bp


app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

# Register blueprints
app.register_blueprint(admin_bp, url_prefix="/api/admin")
app.register_blueprint(police_bp, url_prefix="/api/police")
app.register_blueprint(report_bp, url_prefix="/api/report")
app.register_blueprint(recovered_bp, url_prefix="/api/recovered")


@app.route("/")
def index():
    return {"message": "National Vehicle Recovery API running"}


if __name__ == "__main__":
    app.run(debug=True)

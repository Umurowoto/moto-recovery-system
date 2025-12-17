from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app import models
    from app.routes import (
        admin_routes,
        police_routes,
        report_routes,
        recovered_routes
    )

    app.register_blueprint(admin_routes.admin_bp, url_prefix="/api/admin")
    app.register_blueprint(police_routes.police_bp, url_prefix="/api/police")
    app.register_blueprint(report_routes.report_bp, url_prefix="/api/report")
    app.register_blueprint(recovered_routes.recovered_bp, url_prefix="/api/recovered")

    return app

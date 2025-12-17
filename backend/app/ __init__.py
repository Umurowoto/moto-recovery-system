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

    from app.routes.admin_routes import admin_bp
    from app.routes.police_routes import police_bp
    from app.routes.report_routes import report_bp
    from app.routes.recovered_routes import recovered_bp

    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(police_bp, url_prefix="/api/police")
    app.register_blueprint(report_bp, url_prefix="/api/report")
    app.register_blueprint(recovered_bp, url_prefix="/api/recovered")

    @app.route("/")
    def index():
        return {"message": "National Vehicle Recovery API running"}

    return app

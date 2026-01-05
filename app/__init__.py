from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from app.routes.events import events_bp
    from app.routes.resources import resources_bp
    from app.routes.allocations import allocations_bp
    from app.routes.report import report_bp

    app.register_blueprint(events_bp)
    app.register_blueprint(resources_bp)
    app.register_blueprint(allocations_bp)
    app.register_blueprint(report_bp)

    with app.app_context():
        db.create_all()

    return app

from flask import Flask
from flask_jwt_extended import JWTManager

from app.database.database import db
from app.resources import register_main_blueprint
from config import get_configuration


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(get_configuration())

    db.init_app(app)

    with app.app_context():
        from app.database.models.event import Event
        from app.database.models.event_participant import EventParticipant
        from app.database.models.user import User

        db.create_all()

    register_main_blueprint(app)

    JWTManager(app)

    return app

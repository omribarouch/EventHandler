from flask import Flask
from flask_jwt_extended import JWTManager

# from app.database.database import db
from app.resources import register_main_blueprint
from config import get_configuration


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(get_configuration())

    jwt = JWTManager(app)

    # db.init_app(app)
    # db.create_all()


    register_main_blueprint(app)
    return app

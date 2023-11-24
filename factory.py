from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from app.resources import register_main_blueprint
from config import get_configuration


app = Flask(__name__)
app.config.from_object(get_configuration())

db = SQLAlchemy(app)

register_main_blueprint(app)

JWTManager(app)

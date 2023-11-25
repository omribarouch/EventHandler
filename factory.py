from typing import Type

from celery import Celery
from flask import Flask
from flask_jwt_extended import JWTManager

from app.custom_tasks import SqlAlchemyTask
from app.database import db
from app.logger import logger
from app.mail import mail
from app.resources import register_main_blueprint
from app.socketio import socketio
from config import get_configuration


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(get_configuration())

    db.init_app(app)
    mail.init_app(app)
    socketio.init_app(app)

    with app.app_context():
        db.create_all()
        logger.setLevel(app.config['LOG_LEVEL'])

    register_main_blueprint(app)

    JWTManager(app)

    return app


def create_celery() -> Celery:
    celery = Celery(__name__, task_cls=SqlAlchemyTask)
    celery.config_from_object(get_configuration())
    celery.conf.update(celery.conf['CELERY_CONFIG'])

    return celery

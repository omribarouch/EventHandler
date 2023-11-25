from typing import Type

from celery import Celery
from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO

from app.custom_tasks import SqlAlchemyTask
from app.database import db
from app.logger import logger
from app.mail import mail
from app.resources import register_main_blueprint
from app.socketio import socketio
from config import get_configuration, BaseConfig


def create_app(configuration: Type[BaseConfig] | None = None) -> tuple[Flask, SocketIO]:
    app = Flask(__name__)
    app.config.from_object(configuration if configuration else get_configuration())

    db.init_app(app)
    mail.init_app(app)
    socketio.init_app(app)

    with app.app_context():
        db.create_all()
        logger.setLevel(app.config['LOG_LEVEL'])

    register_main_blueprint(app)

    JWTManager(app)

    return app, socketio


def create_celery(configuration: Type[BaseConfig] | None = None) -> Celery:
    celery = Celery(__name__, task_cls=SqlAlchemyTask)
    celery.config_from_object(configuration if configuration else get_configuration())
    celery.conf.update(celery.conf['CELERY_CONFIG'])

    return celery

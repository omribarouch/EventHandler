import logging
import os
from datetime import timedelta
from typing import Type

from app.celerybeat_config import beat_schedule


class BaseConfig:
    # SqlAlchemy configurations
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT configurations
    JWT_HEADER_TYPE = 'JWT'
    JWT_TOKEN_LOCATION = 'headers'
    JWT_HEADER_NAME = 'Authorization'
    JWT_SECRET_KEY = 'top secret stuff'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)

    # Mail Server configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Event Handler System', MAIL_USERNAME)

    # Logging configurations
    LOG_FORMAT = '%(asctime)s\t%(name)s\t%(levelname)-8s - %(message)s'
    LOG_LEVEL = os.getenv('LOG_LEVEL') or logging.DEBUG

    # Celery configuration
    REDIS_URL = os.getenv('REDIS_URL')
    CELERY_CONFIG = dict(
        accept_content=['pickle', 'json', 'msgpack', 'yaml'],
        task_store_errors_even_if_ignored=True,
        result_backend_transport_options={'master_name': 'mymaster'},
        result_expires=timedelta(hours=1).seconds,
        worker_proc_alive_timeout=60,

        broker_url=f'{REDIS_URL}/0',
        result_backend=f'{REDIS_URL}/0',
        redbeat_redis_url=f'{REDIS_URL}/1',
        redbeat_lock_timeout=60,
        beat_schedule=beat_schedule
    )


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///:memory:'


def get_configuration_by_name(configuration_name: str) -> Type[BaseConfig]:
    return {
        'DEVELOPMENT': DevConfig,
        'PRODUCTION': ProdConfig,
        'DEFAULT': TestConfig,
        'TEST': TestConfig
    }[configuration_name]


def get_configuration() -> Type[BaseConfig]:
    configuration_name: str = os.getenv('FLASK_CONFIGURATION', 'DEFAULT')
    return get_configuration_by_name(configuration_name)

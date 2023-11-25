import os
from datetime import timedelta
from typing import Type


class BaseConfig(object):
    # SqlAlchemy configurations
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis configuration
    REDIS_URL = os.getenv('REDIS_URL')

    # JWT configurations
    JWT_HEADER_TYPE = 'JWT'
    JWT_TOKEN_LOCATION = 'headers'
    JWT_HEADER_NAME = 'Authorization'
    JWT_SECRET_KEY = 'top secret stuff'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)

    # Mail server setting
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    pass


def get_configuration() -> Type[BaseConfig]:
    environment: str = os.getenv('FLASK_CONFIGURATION', 'DEFAULT')
    return {
        'DEVELOPMENT': DevConfig,
        'PRODUCTION': ProdConfig,
        'DEFAULT': DevConfig,
        'TEST': TestConfig
    }[environment]

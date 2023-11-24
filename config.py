import os
from datetime import timedelta
from typing import Type


class BaseConfig(object):
    # SqlAlchemy configurations
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis configuration
    REDIS_URI = 'redis://localhost:6379:0'

    # JWT configurations
    JWT_SECRET_KEY = 'top secret stuff'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)

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

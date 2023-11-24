import os
from typing import Type


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or 'postgresql://your_username:your_password@localhost/your_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'top secret stuff'


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

from flask import Flask, Blueprint
from flask_restful import Api


def register_main_blueprint(app: Flask) -> None:
    from app.resources.event import EventApi
    from app.resources.user import UserApi
    from app.resources.user_login import UserLoginApi

    api: Api = Api(catch_all_404s=True)
    api.add_resource('/events', EventApi)
    api.add_resource('/user', UserApi)
    api.add_resource('/login', UserLoginApi)

    api_bp: Blueprint = Blueprint('api_bp', __name__)
    api.init_app(api_bp)

    app.register_blueprint(blueprint=api_bp)

from flask import Flask, Blueprint
from flask_restful import Api


def register_main_blueprint(app: Flask) -> None:
    from app.resources.event import EventApi
    from app.resources.event import UserApi
    from app.resources.event import UserLoginApi

    api: Api = Api(catch_all_404s=True)
    api.add_resource('/events', EventApi)

    api_bp: Blueprint = Blueprint('api_bp', __name__)
    api.init_app(api_bp)

    app.register_blueprint(blueprint=api_bp)

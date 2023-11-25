from flask import Flask, Blueprint
from flask_restful import Api


def register_main_blueprint(app: Flask) -> None:
    from app.resources.index import IndexApi
    from app.resources.event import EventApi
    from app.resources.event import EventsApi
    from app.resources.event import EventSubscriptionApi
    from app.resources.user import UsersApi
    from app.resources.user_login import UserLoginApi

    api: Api = Api(catch_all_404s=True)
    api_bp: Blueprint = Blueprint('api_bp', __name__)
    api.init_app(api_bp)

    api.add_resource(IndexApi, '/')
    api.add_resource(EventApi, '/events/<int:id>')
    api.add_resource(EventSubscriptionApi, '/events/<int:id>/subscribe')
    api.add_resource(EventsApi, '/events')
    api.add_resource(UsersApi, '/users')
    api.add_resource(UserLoginApi, '/login')

    app.register_blueprint(blueprint=api_bp)


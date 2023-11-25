from flask import Flask, Blueprint
from flask_restx import Api

api_bp: Blueprint = Blueprint('api', __name__)
api: Api = Api(api_bp)


def register_main_blueprint(app: Flask) -> None:
    from app.resources.event import EventApi
    from app.resources.event import EventsApi
    from app.resources.event import EventSubscriptionApi
    from app.resources.user import UsersApi
    from app.resources.user_login import UserLoginApi

    api.add_resource(EventApi, '/events/<int:id>')
    api.add_resource(EventSubscriptionApi, '/events/<int:id>/subscribe')
    api.add_resource(EventsApi, '/events')
    api.add_resource(UsersApi, '/users')
    api.add_resource(UserLoginApi, '/login')

    app.register_blueprint(api_bp, url_prefix='/api')


from http import HTTPStatus

from flask_jwt_extended import create_access_token
from flask_restful import Resource

from app.database.models.user import User
from app.resources.decorators import load_schema
from app.resources.schemas.user_login import UserLoginSchema


class UserLoginApi(Resource):
    @load_schema(UserLoginSchema)
    def post(self, user: User, **kwargs):
        return f'JWT {create_access_token(identity=user.username)}', HTTPStatus.OK

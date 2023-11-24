from flask_api import status
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from app.database.models.user import User
from app.resources.decorators import load_schema
from app.resources.schemas.user_login import UserLoginSchema


class UserLoginApi(Resource):
    @load_schema(UserLoginSchema)
    def post(self, user: User, **kwargs):
        return create_access_token(identity=user.user_name), status.HTTP_200_OK

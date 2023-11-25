from http import HTTPStatus

from flask_restx import abort
from marshmallow import fields, validates_schema
from marshmallow.schema import BaseSchema

from app.database.models.user import User
from app.resources.schemas.fields import UserField


class UserLoginSchema(BaseSchema):
    user: User = UserField(data_key='username', required=True)
    password: str = fields.Str(required=True)

    @validates_schema
    def validate_user_password(self, data, **kwargs):
        user: User = data['user']

        if user.password != data['password']:
            abort(HTTPStatus.BAD_REQUEST, message=f"The password entered for user {user.display_name} is incorrect, "
                                                  f"please try again.")

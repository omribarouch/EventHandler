from http import HTTPStatus

from flask_restx import abort
from marshmallow import fields, validates_schema
from marshmallow.schema import BaseSchema

from app.database import db
from app.database.models.user import User


class PostUserSchema(BaseSchema):
    username: str = fields.Str(required=True)
    display_name: str = fields.Str(data_key='displayName', required=True)
    password: str = fields.Str(required=True)
    email: str = fields.Email(required=True)
    is_admin: bool = fields.Boolean(data_key='isAdmin', required=False, load_default=False)

    @validates_schema
    def validate_username_not_exit(self, data, **kwargs):
        user: User = db.session.query(User).filter(User.username == data['username']).scalar()

        if user is not None:
            abort(HTTPStatus.BAD_REQUEST, message=f"The username {data['username']} is already taken.")

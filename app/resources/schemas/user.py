from marshmallow import fields
from marshmallow.schema import BaseSchema


class PostUserSchema(BaseSchema):
    user_name: str = fields.Str(data_key='userName', required=True)
    display_name: str = fields.Str(data_key='displayName', required=True)
    password: str = fields.Str(required=True)

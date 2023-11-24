from marshmallow import fields
from marshmallow.schema import BaseSchema


class PostUserSchema(BaseSchema):
    username: str = fields.Str(data_key='username', required=True)
    display_name: str = fields.Str(data_key='displayName', required=True)
    password: str = fields.Str(required=True)

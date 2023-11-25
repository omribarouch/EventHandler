from marshmallow import fields
from marshmallow.schema import BaseSchema


class PostUserSchema(BaseSchema):
    username: str = fields.Str(required=True)
    display_name: str = fields.Str(data_key='displayName', required=True)
    password: str = fields.Str(required=True)
    email: str = fields.Email(required=True)
    is_admin: bool = fields.Boolean(data_key='isAdmin', required=False, load_default=False)

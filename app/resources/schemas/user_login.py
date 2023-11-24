from marshmallow.schema import BaseSchema

from app.database.models.user import User
from app.resources.schemas.fields import UserField


class UserLoginSchema(BaseSchema):
    user: User = UserField(data_key='userName', required=True)

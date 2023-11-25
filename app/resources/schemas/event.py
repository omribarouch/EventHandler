from datetime import datetime

from marshmallow import fields
from marshmallow.schema import BaseSchema
from marshmallow.validate import OneOf

from app.database.models.event import Event
from app.database.models.user import User
from app.resources.schemas.fields import EventField, UserField


class GetEventsSchema(BaseSchema):
    sort_by: str = fields.Str(required=False, load_default=None, validate=OneOf(['date', 'creation_time', 'popularity']))
    order: str = fields.Str(required=False, load_default='asc', validate=OneOf(['asc', 'desc']))
    location: str = fields.Str(required=False, load_default=None)


class GetEventSchema(BaseSchema):
    event: Event = EventField(data_key='id', required=True)


class PostEventSchema(BaseSchema):
    name: str = fields.Str(required=True)
    description: str = fields.Str(required=True)
    location: str = fields.Str(required=True)
    date: datetime = fields.DateTime(required=True)
    participants: list[User] = fields.List(cls_or_instance=UserField, required=False, load_default=[])


class PutEventSchema(GetEventSchema):
    name: str = fields.Str(load_default=None)
    description: str = fields.Str(load_default=None)
    location: str = fields.Str(load_default=None)
    date: datetime = fields.DateTime(load_default=None)
    participants: list[User] = fields.List(cls_or_instance=UserField, required=False, load_default=[])


class DeleteEventSchema(GetEventSchema):
    pass

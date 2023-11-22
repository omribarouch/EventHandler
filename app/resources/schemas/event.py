import datetime

from marshmallow import fields
from marshmallow.schema import BaseSchema

from app.database.models.event import Event
from app.resources.schemas.fields import EventField


class GetEventSchema(BaseSchema):
    event: Event = EventField(data_key='id', required=True)


class PostEventSchema(BaseSchema):
    name: str = fields.Str(required=True)
    description: str = fields.Str(required=True)
    date: datetime.date = fields.Date(required=True)


class PutEventSchema(GetEventSchema):
    event: Event = EventField(data_key='id', required=True)
    name: str = fields.Str(default=None)
    description: str = fields.Str(default=None)
    date: datetime.date = fields.Date(default=None)


class DeleteEventSchema(GetEventSchema):
    pass

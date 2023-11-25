import datetime
from http import HTTPStatus

from flask_restful import abort
from marshmallow import fields, validates_schema
from marshmallow.schema import BaseSchema
from marshmallow.validate import OneOf

from app.database.models.event import Event
from app.resources.schemas.fields import EventField


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
    date: datetime.date = fields.DateTime(required=True)


class PutEventSchema(GetEventSchema):
    name: str = fields.Str(default=None)
    description: str = fields.Str(default=None)
    date: datetime.date = fields.Date(default=None)


class DeleteEventSchema(GetEventSchema):
    pass

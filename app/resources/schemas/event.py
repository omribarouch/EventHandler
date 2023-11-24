import datetime
from http import HTTPStatus

from flask_restful import abort
from marshmallow import fields, validates_schema
from marshmallow.schema import BaseSchema

from app.database.models.event import Event
from app.resources.schemas.fields import EventField


class GetEventsSchema(BaseSchema):
    sort_by: str = fields.Str(required=False, load_default=None)
    order: str = fields.Str(required=False, load_default='asc')
    location: str = fields.Str(required=False, load_default=None)

    @validates_schema
    def validate_sort_criteria(self, data, **kwargs):
        allowed_values: list[str] = ['date', 'creation_time', 'popularity']
        if data['sort_by'] and data['sort_by'] not in allowed_values:
            abort(HTTPStatus.BAD_REQUEST, error=f"Invalid sort_by parameter. Use one of: {allowed_values}")

    @validates_schema
    def validate_order(self, data, **kwargs):
        allowed_values: list[str] = ['asc', 'dsc']
        if data['order'] not in allowed_values:
            abort(HTTPStatus.BAD_REQUEST, error=f"Invalid order parameter. Use one of: {allowed_values}")


class GetEventSchema(BaseSchema):
    event: Event = EventField(data_key='id', required=True)


class PostEventSchema(BaseSchema):
    name: str = fields.Str(required=True)
    description: str = fields.Str(required=True)
    location: str = fields.Str(required=True)
    date: datetime.date = fields.DateTime(required=True)


class PutEventSchema(GetEventSchema):
    event: Event = EventField(data_key='id', required=True)
    name: str = fields.Str(default=None)
    description: str = fields.Str(default=None)
    date: datetime.date = fields.Date(default=None)


class DeleteEventSchema(GetEventSchema):
    pass

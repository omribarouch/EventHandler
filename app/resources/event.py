import datetime

from flask import g
from flask_api import status
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, abort

from app.database.database import db
from app.database.models.event import Event
from app.logger import logger
from app.resources.decorators import load_schema
from app.resources.schemas.event import GetEventSchema, PostEventSchema, PutEventSchema, DeleteEventSchema


class EventApi(Resource):
    @jwt_required
    @load_schema(GetEventSchema)
    def get(self, event: Event, **kwargs):
        return event.serialize(), status.HTTP_200_OK

    @jwt_required
    @load_schema(PostEventSchema)
    def post(self, name: str, description: str, location: str, date: datetime.date):
        new_event: Event = Event(name=name,
                                 description=description,
                                 location=location,
                                 date=date)

        try:
            db.session.add(new_event)
            db.session.commit()
            return {'message': 'ok'}, status.HTTP_201_CREATED
        except Exception:
            db.session.rollback()
            logger.exception('Failed to add event',
                             extra=dict(submitter=get_jwt_identity()))
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR, error='Something went wrong while trying '
                                                               'to add new event to the system')

    @jwt_required
    @load_schema(PutEventSchema)
    def put(self, event: Event, name: str, description: str, date: datetime.date, **kwargs):
        event.name = name or event.name
        event.description = description or event.description
        event.date = date or event.date

        try:
            db.session.commit()
            return {'message': 'ok'}, status.HTTP_200_OK
        except Exception:
            db.session.rollback()
            logger.exception(f'Failed to update event #{event.id}',
                             extra=dict(event_id=event.id, submitter=get_jwt_identity()))
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR, error=f'Something went wrong while trying '
                                                               f'to update the event #{event.id}')

    @jwt_required
    @load_schema(DeleteEventSchema)
    def delete(self, event: Event, **kwargs):
        try:
            db.session.delete(event)
            return {'message': 'ok'}, status.HTTP_200_OK
        except Exception:
            db.session.rollback()
            logger.exception(f'Failed to delete event #{event.id}',
                             extra=dict(event_id=event.id, submitter=get_jwt_identity()))
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR, error=f'Something went wrong while trying '
                                                               f'to delete the event #{event.id}')

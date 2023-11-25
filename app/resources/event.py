from datetime import datetime
from http import HTTPStatus

from flask import current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Resource, abort

from app.database.models.socket_event import SocketEvent
from app.database.models.socket_namespace import SocketNamespace
from app.database import db
from app.database.models.event import Event
from app.database.models.user import User
from app.database.queries.event_queries import get_events
from app.logger import logger
from app.resources.decorators import load_schema
from app.resources.schemas.event import GetEventSchema, PostEventSchema, PutEventSchema, DeleteEventSchema, \
    GetEventsSchema
from app.socketio import socketio


class EventsApi(Resource):
    @jwt_required()
    @load_schema(GetEventsSchema)
    def get(self, sort_by: str | None, order: str | None, location: str | None):
        events = get_events(sort_by=sort_by,
                            order=order,
                            location=location)

        return [event.serialize() for event in events], HTTPStatus.OK

    @jwt_required()
    @load_schema(PostEventSchema)
    def post(self, name: str, description: str, location: str, date: datetime, participants: list[User] = []):
        new_event: Event = Event(name=name,
                                 description=description,
                                 location=location,
                                 date=date,
                                 participants=participants)

        try:
            db.session.add(new_event)
            db.session.commit()
            return new_event.serialize(), HTTPStatus.CREATED
        except Exception:
            db.session.rollback()
            logger.exception('Failed to add event',
                             extra=dict(submitter=get_jwt_identity()))
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, message='Something went wrong while trying '
                                                            'to add new event to the system')


class EventApi(Resource):
    @jwt_required()
    @load_schema(GetEventSchema)
    def get(self, event: Event):
        return event.serialize(), HTTPStatus.OK

    @jwt_required()
    @load_schema(PutEventSchema)
    def put(self, event: Event, name: str, description: str, location: str, date: datetime, participants: list[User] = []):
        event.name = name or event.name
        event.description = description or event.description
        event.location = location or event.location
        event.date = date or event.date
        event.participants = participants or event.participants

        try:
            db.session.commit()
            socketio.emit(event=SocketEvent.DELETE,
                          data=event,
                          namespace=SocketNamespace.EVENT,
                          room=event.id)
            return event.serialize(), HTTPStatus.OK
        except Exception:
            db.session.rollback()
            logger.exception(f'Failed to update event #{event.id}',
                             extra=dict(event_id=event.id, submitter=get_jwt_identity()))
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, message=f'Something went wrong while trying '
                                                            f'to update the event #{event.id}')

    @jwt_required()
    @load_schema(DeleteEventSchema)
    def delete(self, event: Event):
        try:
            with current_app.app_context():
                db.session.delete(event)
                db.session.commit()
                socketio.emit(event=SocketEvent.DELETE,
                              data=event,
                              namespace=SocketNamespace.EVENT,
                              room=event.id)
            return {'message': 'ok'}, HTTPStatus.OK
        except Exception:
            with current_app.app_context():
                db.session.rollback()
            logger.exception(f'Failed to delete event #{event.id}',
                             extra=dict(event_id=event.id, submitter=get_jwt_identity()))
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, message=f'Something went wrong while trying '
                                                            f'to delete the event #{event.id}')


class EventSubscriptionApi(Resource):
    @load_schema(GetEventSchema)
    def post(self, event: Event):
        socketio.emit('leave', namespace=SocketNamespace.EVENT, room=event.id)
        return {'message': 'ok'}, HTTPStatus.OK

    @load_schema(GetEventSchema)
    def delete(self, event: Event):
        socketio.emit('leave', namespace=SocketNamespace.EVENT, room=event.id)
        return {'message': 'ok'}, HTTPStatus.OK
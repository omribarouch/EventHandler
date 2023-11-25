from http import HTTPStatus

from flask_restx import abort
from marshmallow import fields
from app.database.models.event import Event
from app.database.models.user import User
from app.database.queries.event_queries import get_event_by_id
from app.database.queries.user_queries import get_user_by_username


class EventField(fields.Integer):
    def _deserialize(self, value, attr, data, **kwargs) -> Event:
        event_id: int = super()._deserialize(value, attr, data)

        event: Event | None = get_event_by_id(event_id)
        if event is None:
            abort(HTTPStatus.NOT_FOUND, message=f"Event #{id} wasn't found")

        return event


class UserField(fields.Str):
    def _deserialize(self, value, attr, data, **kwargs) -> User:
        username: str = super()._deserialize(value, attr, data)
        user: User | None = get_user_by_username(username)
        if user is None:
            abort(HTTPStatus.NOT_FOUND, message=f"User #{username} wasn't found")

        return user

from http import HTTPStatus
from typing import TypeVar, Generic

from flask_restful import abort
from marshmallow import fields
from marshmallow.fields import Field

from app.database import Model
from app.database import db
from app.database.models.event import Event
from app.database.models.user import User

F = TypeVar('F', bound=Field)
M = TypeVar('M', bound=Model)


class ModelField(Generic[F, M]):
    def _deserialize(self, value, attr, data, **kwargs) -> M:
        model_identifier: any = F()._deserialize(value, attr, data)
        model: M = db.session.query(M).filter_by(id=model_identifier).scalar()
        if model is None:
            abort(HTTPStatus.NOT_FOUND, error=f"{M.__class__} #{model_identifier} wasn't found")

        return model


class EventField(fields.Integer):
    def _deserialize(self, value, attr, data, **kwargs) -> Event:
        event_id: int = super()._deserialize(value, attr, data)

        event: Event | None = db.session.query(Event).filter(Event.id == event_id).scalar()
        if event is None:
            abort(HTTPStatus.NOT_FOUND, error=f"Event #{id} wasn't found")

        return event


class UserField(fields.Str):
    def _deserialize(self, value, attr, data, **kwargs) -> User:
        username: str = super()._deserialize(value, attr, data)
        user: User | None = db.session.query(User).filter(User.username == username).scalar()
        if user is None:
            abort(HTTPStatus.NOT_FOUND, error=f"User #{username} wasn't found")

        return user

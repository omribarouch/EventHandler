from flask_api import status
from flask_restful import abort
from marshmallow import fields

from app.database.database import db
from app.database.models.event import Event


class EventField(fields.Integer):
    def _deserialize(self, value, attr, data, **kwargs) -> Event:
        event_id: int = super()._deserialize(value, attr, data)
        event: Event | None = db.session.query(Event).filter_by(id=event_id).scalar()
        if event is None:
            abort(status.HTTP_404_NOT_FOUND, error=f"Event #{id} wasn't found")

        return event

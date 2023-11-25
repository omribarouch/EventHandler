from sqlalchemy import Column, func
from sqlalchemy.orm import Query, joinedload

from app.database import db
from app.database.models.event import Event
from app.database.models.event_participant import EventParticipant
from app.database.models.user import User


def get_events(sort_by: str | None, order: str | None, location: str | None) -> list[Event]:
    base_query: Query = db.session.query(Event)

    if location:
        base_query = base_query.filter(Event.location == location)

    if sort_by:
        sort_column: Column
        if sort_by == 'popularity':
            sort_column = func.count(User.username)
            base_query = base_query.outerjoin(EventParticipant) \
                .options(joinedload(Event.participants)).group_by(Event.id)
        else:
            sort_column = getattr(Event, sort_by, None)

        base_query = base_query.order_by(getattr(sort_column, order)())

    return base_query.all()

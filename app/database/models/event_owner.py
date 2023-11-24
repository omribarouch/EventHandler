from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Model
from app.database.models.event import Event
from app.database.models.user import User


class EventOwner(Model):
    __tablename__ = 'EventParticipant'

    user_id: Column | int = Column('UserID', Integer, ForeignKey('User.id'), primary_key=True)
    user: User = relationship('User')
    event_id: Column | int = Column('EventID', Integer, ForeignKey('Event.id'), primary_key=True)
    event: Event = relationship('Event')

    def __init__(self,
                 user: User,
                 event: Event):
        self.user = user
        self.event = event

    def serialize(self) -> dict:
        return {
            'user': self.user.serialize(),
            'event': self.event.serialize(),
        }

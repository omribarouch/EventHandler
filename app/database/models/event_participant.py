from sqlalchemy import Column, Integer, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship
from factory import db


class EventParticipant(db.Model):
    __tablename__ = 'EventParticipant'

    username: Column | str = Column('Username', VARCHAR(20), ForeignKey('User.Username'), primary_key=True)
    user: 'User' = relationship('User')
    event_id: Column | int = Column('EventID', Integer, ForeignKey('Event.ID'), primary_key=True)
    event: 'Event' = relationship('Event')

    def __init__(self,
                 user: 'User',
                 event: 'Event'):
        self.user = user
        self.event = event

    def serialize(self) -> dict:
        return {
            'user': self.user.serialize(),
            'event': self.event.serialize(),
        }

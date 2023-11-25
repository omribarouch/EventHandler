from datetime import timedelta, datetime
from sqlalchemy import Column, Integer, VARCHAR, DateTime, Boolean
from sqlalchemy.orm import relationship

from app.database import Model
from app.database.models.event_participant import EventParticipant


class Event(Model):
    __tablename__: str = 'Event'

    id: Column | int = Column('ID', Integer, primary_key=True, autoincrement=True)
    name: Column | str = Column('Name', VARCHAR(50), nullable=False)
    description: Column | str = Column('Description', VARCHAR(200), nullable=False)
    location: Column | str = Column('Location', VARCHAR(100), nullable=False, index=True)
    date: Column | datetime = Column('Date', DateTime, nullable=False, index=True)
    creation_time: Column | datetime = Column('CreationTime', DateTime, default=datetime.now(),
                                                   nullable=False, index=True)
    notified: Column | bool = Column('Notified', Boolean, nullable=False, default=False)
    participants: list['User'] = relationship('User', secondary=EventParticipant.__tablename__,
                                              back_populates="events", lazy="select",
                                              overlaps="user,event")

    def __init__(self,
                 name: str,
                 description: str,
                 location: str,
                 date: datetime):
        self.name = name
        self.description = description
        self.location = location
        self.date = date

    def is_notification_required(self):
        return datetime.now() >= Event.date - timedelta(minutes=30) and self.notified

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'date': str(self.date),
            'creationTime': str(self.creation_time),
            'participants': [participant.display_name for participant in self.participants]
        }

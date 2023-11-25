import datetime

from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.util import hybridproperty

from app.database.base import Model
from app.database.models.event_participant import EventParticipant


class Event(Model):
    __tablename__: str = 'Event'

    id: Column | int = Column('ID', Integer, primary_key=True, autoincrement=True)
    name: Column | str = Column('Name', VARCHAR(50), nullable=False)
    description: Column | str = Column('Description', VARCHAR(200), nullable=False)
    location: Column | str = Column('Location', VARCHAR(100), nullable=False, index=True)
    date: Column | datetime.date = Column('Date', DateTime, nullable=False, index=True)
    creation_time: Column | datetime.date = Column('CreationTime', DateTime,
                                                   default=datetime.datetime.now(), nullable=False, index=True)
    participants: list['User'] = relationship('User', secondary=EventParticipant.__tablename__,
                                              back_populates="events", lazy="select",
                                              overlaps="user,event")

    def __init__(self,
                 name: str,
                 description: str,
                 location: str,
                 date: datetime.date):
        self.name = name
        self.description = description
        self.location = location
        self.date = date

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

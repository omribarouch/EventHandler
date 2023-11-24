import datetime

from sqlalchemy import Column, Integer, Date, NVARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.util import hybridproperty

from app.database.base import Model
from app.database.models.event_participant import EventParticipant
from app.database.models.user import User


class Event(Model):
    __tablename__ = 'Event'

    id: Column | int = Column('ID', Integer, primary_key=True, autoincrement=True)
    name: Column | str = Column('Name', NVARCHAR(50), nullable=False)
    description: Column | str = Column('Description', NVARCHAR(200), nullable=False)
    location: Column | str = Column('Location', NVARCHAR(100), nullable=False)
    date: Column | datetime.date = Column('Date', Date, nullable=False)
    creation_time: Column | datetime.date = Column('CreationTime', Date,
                                                   default=datetime.datetime.utcnow(), nullable=False)
    creators: list[User] = relationship(User)
    participants: list[User] = relationship(User, secondary=EventParticipant.__tablename__, backref='Event')

    def __init__(self,
                 name: str,
                 description: str,
                 location: str,
                 date: datetime.date):
        self.name = name
        self.description = description
        self.location = location
        self.date = date

    @hybridproperty
    def popularity(self) -> int:
        return len(self.participants)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'date': str(self.date),
            'creationTime': str(self.creation_time),
            'popularity': self.popularity
        }

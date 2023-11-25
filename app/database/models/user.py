from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import relationship

from app.database.base import Model
from app.database.models.event_participant import EventParticipant


class User(Model):
    __tablename__ = 'User'

    username: Column | str = Column('Username', VARCHAR(20), primary_key=True)
    password: Column | str = Column("Password", VARCHAR(20), nullable=False)
    display_name: Column | str = Column('DisplayName', VARCHAR(30), nullable=False)
    email: Column | str = Column('Email', VARCHAR(30), nullable=False)
    events: list['Event'] = relationship('Event', secondary=EventParticipant.__tablename__,
                                         back_populates="participants", lazy="select",
                                         overlaps="event,user")

    def __init__(self,
                 username: str,
                 password: str,
                 display_name: str,
                 email: str):
        self.username = username
        self.password = password
        self.display_name = display_name
        self.email = email

    def serialize(self) -> dict:
        return {
            'username': self.username,
            'password': self.password,
            'displayName': self.display_name,
            'email': self.email
        }

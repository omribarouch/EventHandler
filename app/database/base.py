from abc import abstractmethod

from sqlalchemy.ext.declarative import declarative_base

from app.database.database import db


class Model(db.Model):
    __abstract__ = True

    @property
    def __tablename__(self) -> str:
        pass

    @abstractmethod
    def serialize(self) -> dict:
        pass

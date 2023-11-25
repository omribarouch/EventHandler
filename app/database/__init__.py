from abc import abstractmethod, abstractproperty

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Model(db.Model):
    __abstract__ = True

    @abstractproperty
    def __tablename__(self) -> str:
        pass

    @abstractmethod
    def serialize(self) -> dict:
        pass

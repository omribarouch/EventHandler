from abc import abstractmethod

from sqlalchemy.ext.declarative import declarative_base


class Model():
    __abstract__ = True

    @property
    def __tablename__(self) -> str:
        pass

    @abstractmethod
    def serialize(self) -> dict:
        pass

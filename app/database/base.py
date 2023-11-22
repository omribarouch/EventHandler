from abc import ABC, abstractmethod

from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class Model(ABC):
    @abstractmethod
    @property
    def __tablename__(self) -> str:
        pass

    @abstractmethod
    def serialize(self) -> dict:
        pass

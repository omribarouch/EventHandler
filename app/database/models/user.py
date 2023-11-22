from sqlalchemy import Column, Integer, NVARCHAR

from app.database.base import Model


class User(Model):
    __tablename__ = 'User'

    id: Column | int = Column('ID', Integer, primary_key=True, autoincrement=True)
    name: Column | str = Column('Name', NVARCHAR(50), nullable=False)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name
        }

from sqlalchemy import Column, NVARCHAR

from app.database.base import Model


class User(Model):
    __tablename__ = 'User'

    user_name: Column | str = Column('UserName', NVARCHAR(50), primary_key=True)
    display_name: Column | str = Column('DisplayName', NVARCHAR(50), nullable=False)
    password: Column | str = Column("Password", NVARCHAR(100), nullable=False)

    def __init__(self,
                 user_name: str,
                 display_name: str,
                 password: str):
        self.user_name = user_name
        self.display_name = display_name
        self.password = password

    def serialize(self) -> dict:
        return {
            'userName': self.user_name,
            'displayName': self.display_name,
            'password': self.password
        }

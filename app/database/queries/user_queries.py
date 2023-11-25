from app.database import db
from app.database.models.user import User


def get_user_by_username(username: str) -> User | None:
    return db.session.query(User).filter(User.username == username).scalar()

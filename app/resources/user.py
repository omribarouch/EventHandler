from http import HTTPStatus

from flask_restx import Resource, abort

from app.database import db
from app.database.models.user import User
from app.logger import logger
from app.resources.decorators import load_schema
from app.resources.schemas.user import PostUserSchema


class UsersApi(Resource):
    @load_schema(PostUserSchema)
    def post(self, username: str, display_name: str, password: str, email: str, is_admin: bool):
        new_user: User = User(username=username,
                              display_name=display_name,
                              password=password,
                              email=email,
                              is_admin=is_admin)

        try:
            db.session.add(new_user)
            db.session.commit()
            return new_user.serialize(), HTTPStatus.CREATED
        except Exception:
            db.session.rollback()
            logger.exception('Failed to add User')
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, message='Something went wrong while trying '
                                                            'to add new user to the system')

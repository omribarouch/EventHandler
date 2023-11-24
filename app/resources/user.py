from http import HTTPStatus

from flask_restful import Resource, abort

from factory import db
from app.database.models.user import User
from app.logger import logger
from app.resources.decorators import load_schema
from app.resources.schemas.user import PostUserSchema


class UsersApi(Resource):
    @load_schema(PostUserSchema)
    def post(self, username: str, display_name: str, password: str):
        new_user: User = User(username=username,
                              display_name=display_name,
                              password=password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return new_user.serialize(), HTTPStatus.CREATED
        except Exception:
            db.session.rollback()
            logger.exception('Failed to add User')
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, error='Something went wrong while trying '
                                                          'to add new user to the system')

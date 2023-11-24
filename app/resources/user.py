from flask_api import status
from flask_restful import Resource, abort

from app.database.database import db
from app.database.models.user import User
from app.logger import logger
from app.resources.decorators import load_schema
from app.resources.schemas.user import PostUserSchema


class UserApi(Resource):
    @load_schema(PostUserSchema)
    def post(self, user_name: str, display_name: str, password: str):
        new_user: User = User(user_name=user_name,
                              display_name=display_name,
                              password=password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return new_user.serialize(), status.HTTP_201_CREATED
        except Exception:
            db.session.rollback()
            logger.exception('Failed to add User')
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR, error='Something went wrong while trying '
                                                               'to add new user to the system')

from http import HTTPStatus

from flask_restful import Resource, abort

from factory import db, app


class IndexApi(Resource):
    def get(self):
        from app.database.models.event import Event
        from app.database.models.user import User
        from app.database.models.event_participant import EventParticipant

        try:
            with app.app_context():
                db.create_all()
            return {'message': 'Tables created successfully'}, HTTPStatus.OK
        except Exception as e:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, error=f"Error creating tables: {str(e)}")

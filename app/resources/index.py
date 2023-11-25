from http import HTTPStatus

from flask_restful import Resource


class IndexApi(Resource):
    def get(self):
        return {'App': 'Event Handler'}, HTTPStatus.OK

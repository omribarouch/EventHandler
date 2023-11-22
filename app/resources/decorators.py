from functools import wraps
from typing import Type

from flask import request
from flask_api import status
from marshmallow import EXCLUDE, ValidationError
from marshmallow.schema import BaseSchema


def load_schema(schema: Type[BaseSchema]):
    def wrap(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            try:
                schema_instance: dict = schema().load(
                    {
                        **(request.get_json(silent=True) or {}),
                        **request.view_args,
                        **request.args.to_dict()
                    },
                    unknown=EXCLUDE
                )

                return f(*args, **schema_instance)
            except ValidationError as e:
                return {'error': e.messages}, status.HTTP_400_BAD_REQUEST

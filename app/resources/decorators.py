from functools import wraps
from http import HTTPStatus
from typing import Type

from flask import request
from marshmallow import EXCLUDE, ValidationError
from marshmallow.schema import BaseSchema


def load_schema(schema: Type[BaseSchema]):
    def decorator(f):
        def wrap(*args, **kwargs):
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
                return {'error': e.messages}, HTTPStatus.BAD_REQUEST

        return wrap

    return decorator

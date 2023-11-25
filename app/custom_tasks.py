from celery import Task
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from config import get_configuration

engine = create_engine(get_configuration().SQLALCHEMY_DATABASE_URI)


class SqlAlchemyTask(Task):
    _scoped_session: scoped_session | None = None
    _flask_app: Flask | None = None

    def __call__(self, *args, **kwargs):
        if not self._flask_app:
            from factory import create_app
            self._flask_app, socketio = create_app()

        with self._flask_app.app_context():
            return self.run(*args, **kwargs)

    @property
    def session(self) -> scoped_session:
        if self._scoped_session is None:
            self._scoped_session = scoped_session(sessionmaker(bind=engine,
                                                               autocommit=False,
                                                               autoflush=False))
        return self._scoped_session

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        if self._scoped_session is not None:
            self._scoped_session.remove()
        super().after_return(status, retval, task_id, args, kwargs, einfo)

from unittest import TestCase

from app.database import db
from config import get_configuration_by_name
from factory import create_app
from test.mock_manager import MockManager


class FlaskInMemoryTest(TestCase):
    def setUp(self):
        self.app, self.socketio = create_app(get_configuration_by_name('TEST'))
        self.app.testing = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.mock_manager = MockManager()

        with self.app_context:
            db.create_all()

    def tearDown(self):
        with self.app_context:
            db.drop_all()
            db.session.remove()

        self.app_context.pop()
        self.mock_manager.deconstruct_patches()

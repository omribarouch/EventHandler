from unittest import TestCase

from app.database.models.event import Event
from test.basic_test_setup import BasicTestSetup


class TestEventParticipant(BasicTestSetup):
    def test_participants_is_empty_array(self):
        self.assertEquals(self.holiday_event.participants, [{}])

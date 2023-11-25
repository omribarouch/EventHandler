import os
from datetime import datetime
from unittest import TestCase

from app.database import db
from app.database.models.event import Event
from app.database.models.user import User
from config import get_configuration_by_name
from factory import create_app
from test.base_flask_test import FlaskInMemoryTest


class BasicTestSetup(FlaskInMemoryTest):
    def setUp(self):
        super().setUp()

        # Add Users
        self.admin_user_username = 'admin'
        self.admin_user_password = 'secret'
        self.admin_user_display_name = 'Admin Admin'
        self.admin_user_email = 'Admin@gmail.com'
        self.admin_user_is_admin = True
        self.admin_user = User(username=self.admin_user_username,
                               password=self.admin_user_password,
                               display_name=self.admin_user_display_name,
                               email=self.admin_user_email,
                               is_admin=self.admin_user_is_admin)

        self.first_user = User(username='omby8888',
                               password='very secret',
                               display_name='Omri Barouch',
                               email='omby8888@gmail.com',
                               is_admin=False)

        self.second_user = User(username='talka4444',
                                password='very secret stuff',
                                display_name='Tal Kahila',
                                email='talka4444@gmail.com',
                                is_admin=False)
        db.session.add_all([self.admin_user, self.first_user, self.second_user])

        # Add events
        self.holiday_event_name = 'Holiday Event'
        self.holiday_event_description = 'Christmas Holiday Event 2023'
        self.holiday_event_location = 'Office'
        self.holiday_event_date = datetime(year=2023, month=12, day=25,
                                           hour=17, minute=0)
        self.holiday_event = Event(name=self.holiday_event_name,
                                   description=self.holiday_event_description,
                                   location=self.holiday_event_location,
                                   date=self.holiday_event_date)

        self.birthday_event = Event(name='My Birthday!!',
                                    description="Omri's Birthday",
                                    location='Binyamina',
                                    date=datetime(year=2024, month=8, day=19))

        self.derby_match_event = Event(name='Maccabi Haifa - Hapoel Haifa',
                                       description='Haifa city derby match',
                                       location='Sammy Offer stadium',
                                       date=datetime(year=2023, month=8, day=30,
                                                     hour=21, minute=30))

        db.session.add_all([self.holiday_event, self.birthday_event, self.derby_match_event])

        # Add event participants


        db.session.commit()

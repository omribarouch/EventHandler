from datetime import datetime
from http import HTTPStatus
from unittest.mock import MagicMock

from app.database.models.event import Event
from test.basic_test_setup import BasicTestSetup


class TestEventsApi(BasicTestSetup):
    def setUp(self):
        super().setUp()

        self.mock_get_events: MagicMock = self.mock_manager.mock('app.database.queries.event_queries.get_events')
        self.mock_get_events_response: list[Event] = [self.holiday_event,
                                                      self.birthday_event,
                                                      self.derby_match_event]
        self.mock_get_events.return_value = self.mock_get_events_response

    def test_get_all_events(self):
        expected_status = HTTPStatus.OK.value
        expected_response = [event.serialize() for event in self.mock_get_events_response]

        response = self.client.get('/api/events', headers={'Authorization': f'JWT {self.first_user_access_token}'})

        self.assertEquals(response.status_code, expected_status)
        self.assertEquals(response.get_json(), expected_response)

    def test_get_all_events_by_non_participating_user(self):
        expected_status = HTTPStatus.OK.value
        expected_response = [event.serialize() for event in self.mock_get_events_response]

        response = self.client.get('/api/events', headers={'Authorization': f'JWT {self.second_user_access_token}'})

        self.assertEquals(response.status_code, expected_status)
        self.assertEquals(response.get_json(), expected_response)

    def test_get_all_events_by_unauthorized_user(self):
        expected_status = HTTPStatus.UNAUTHORIZED.value

        response = self.client.get('/api/events')

        self.assertEquals(response.status_code, expected_status)

    def test_get_all_events_by_non_exist_sort_criterion(self):
        expected_status = HTTPStatus.BAD_REQUEST.value

        response = self.client.get('/api/events?sort_by=something',
                                   headers={'Authorization': f'JWT {self.first_user_access_token}'})

        self.assertEquals(response.status_code, expected_status)

    def test_get_all_events_by_non_exist_order(self):
        expected_status = HTTPStatus.BAD_REQUEST.value

        response = self.client.get('/api/events?order=up',
                                   headers={'Authorization': f'JWT {self.first_user_access_token}'})

        self.assertEquals(response.status_code, expected_status)

    def test_get_all_events_sort_by_date_asc(self):
        expected_status = HTTPStatus.OK.value
        expected_response = [self.derby_match_event.serialize(),
                             self.holiday_event.serialize(),
                             self.birthday_event.serialize()]

        response = self.client.get('/api/events?sort_by=date', headers={'Authorization': f'JWT {self.first_user_access_token}'})

        self.assertEquals(response.status_code, expected_status)
        self.assertEquals(response.get_json(), expected_response)

    def test_get_all_events_sort_by_date_desc(self):
        expected_status = HTTPStatus.OK.value
        expected_response = [self.birthday_event.serialize(),
                             self.holiday_event.serialize(),
                             self.derby_match_event.serialize()]

        response = self.client.get('/api/events?sort_by=date&order=desc',
                                   headers={'Authorization': f'JWT {self.first_user_access_token}'})

        self.assertEquals(response.status_code, expected_status)
        self.assertEquals(response.get_json(), expected_response)

    def test_get_all_events_sort_by_creation_time_asc(self):
        expected_status = HTTPStatus.OK.value
        expected_response = [self.holiday_event.serialize(),
                             self.birthday_event.serialize(),
                             self.derby_match_event.serialize()]

        response = self.client.get('/api/events?sort_by=creation_time',
                                   headers={'Authorization': f'JWT {self.first_user_access_token}'})

        self.assertEquals(response.status_code, expected_status)
        self.assertEquals(response.get_json(), expected_response)

    def test_get_all_events_sort_by_creation_time_desc(self):
        expected_status = HTTPStatus.OK.value
        expected_response = [self.derby_match_event.serialize(),
                             self.birthday_event.serialize(),
                             self.holiday_event.serialize()]

        response = self.client.get('/api/events?sort_by=creation_time&order=desc',
                                   headers={'Authorization': f'JWT {self.first_user_access_token}'})

        self.assertEquals(response.status_code, expected_status)
        self.assertEquals(response.get_json(), expected_response)

    def test_get_all_events_sort_by_popularity_asc(self):
        expected_status = HTTPStatus.OK.value
        expected_response = [self.birthday_event.serialize(),
                             self.derby_match_event.serialize(),
                             self.holiday_event.serialize()]

        response = self.client.get('/api/events?sort_by=popularity',
                                   headers={'Authorization': f'JWT {self.first_user_access_token}'})

        self.assertEquals(response.status_code, expected_status)
        self.assertEquals(response.get_json(), expected_response)

    def test_get_all_events_sort_by_popularity_desc(self):
        expected_status = HTTPStatus.OK.value
        expected_response = [self.holiday_event.serialize(),
                             self.derby_match_event.serialize(),
                             self.birthday_event.serialize()]

        response = self.client.get('/api/events?sort_by=popularity&order=desc',
                                   headers={'Authorization': f'JWT {self.first_user_access_token}'})

        self.assertEquals(response.status_code, expected_status)
        self.assertEquals(response.get_json(), expected_response)

    def test_get_all_events_by_non_existing_location(self):
        expected_status = HTTPStatus.OK.value
        expected_response = []

        response = self.client.get('/api/events?location=nowhere',
                                   headers={'Authorization': f'JWT {self.first_user_access_token}'})

        self.assertEquals(response.status_code, expected_status)
        self.assertEquals(response.get_json(), expected_response)

    def test_get_all_events_by_existing_location(self):
        expected_status = HTTPStatus.OK.value
        expected_response = [self.derby_match_event.serialize()]

        response = self.client.get(f'/api/events?location={self.derby_match_event.location}',
                                   headers={'Authorization': f'JWT {self.first_user_access_token}'})

        self.assertEquals(response.status_code, expected_status)
        self.assertEquals(response.get_json(), expected_response)

    def test_post_event(self):
        expected_status = HTTPStatus.CREATED.value
        new_event: Event = Event(name='new', description='description', location='loc', date=datetime.now())

        response = self.client.post('/api/events',
                                    headers={'Authorization': f'JWT {self.first_user_access_token}'},
                                    json={
                                        'name': new_event.name,
                                        'description': new_event.description,
                                        'location': new_event.location,
                                        'date': str(new_event.date)
                                    })

        self.assertEquals(response.status_code, expected_status)

    def test_post_event_by_unauthorized_user(self):
        expected_status = HTTPStatus.UNAUTHORIZED.value

        response = self.client.post('/api/events')

        self.assertEquals(response.status_code, expected_status)

    def test_post_event_without_name(self):
        expected_status = HTTPStatus.BAD_REQUEST.value

        response = self.client.post('/api/events',
                                    headers={'Authorization': f'JWT {self.first_user_access_token}'},
                                    json={
                                        'description': 'description',
                                        'location': 'location',
                                        'date': str(datetime.now())
                                    })

        self.assertEquals(response.status_code, expected_status)

    def test_post_event_without_description(self):
        expected_status = HTTPStatus.BAD_REQUEST.value

        response = self.client.post('/api/events',
                                    headers={'Authorization': f'JWT {self.first_user_access_token}'},
                                    json={
                                        'name': 'name',
                                        'location': 'location',
                                        'date': str(datetime.now())
                                    })

        self.assertEquals(response.status_code, expected_status)

    def test_post_event_without_date(self):
        expected_status = HTTPStatus.BAD_REQUEST.value

        response = self.client.post('/api/events',
                                    headers={'Authorization': f'JWT {self.first_user_access_token}'},
                                    json={
                                        'name': 'name',
                                        'description': 'description',
                                        'location': 'location',
                                    })

        self.assertEquals(response.status_code, expected_status)

    def test_post_event_without_location(self):
        expected_status = HTTPStatus.BAD_REQUEST.value

        response = self.client.post('/api/events',
                                    headers={'Authorization': f'JWT {self.first_user_access_token}'},
                                    json={
                                        'name': 'name',
                                        'description': 'description',
                                        'date': str(datetime.now())
                                    })

        self.assertEquals(response.status_code, expected_status)


class TestEventApi(BasicTestSetup):
    def test_get_event(self):
        pass

    def test_get_event_non_existing_event_id(self):
        pass

    def test_get_event_by_unparticipated_user(self):
        pass

    def test_get_event_by_unauthorized_user(self):
        pass

    def test_put_event_all_available_attributes(self):
        pass

    def test_put_event_only_name_should_change(self):
        pass

    def test_put_event_only_description_should_change(self):
        pass

    def test_put_event_only_location_should_change(self):
        pass

    def test_put_event_only_date_should_change(self):
        pass

    def test_put_event_non_existing_event_id(self):
        pass

    def test_put_event_by_unparticipated_user(self):
        pass

    def test_put_event_by_unauthorized_user(self):
        pass

    def test_delete_event(self):
        pass

    def test_delete_event_non_existing_event(self):
        pass

    def test_delete_event_by_unparticipated_user(self):
        pass

    def test_delete_event_by_unauthorized_user(self):
        pass

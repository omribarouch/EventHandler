from test.basic_test_setup import BasicTestSetup


class TestEventsApi(BasicTestSetup):
    def test_get_all_events(self):
        pass

    def test_get_all_events_by_non_participating_user(self):
        pass

    def test_get_all_events_by_unauthorized_user(self):
        pass

    def test_get_all_events_sort_by_date_asc(self):
        pass

    def test_get_all_events_sort_by_date_desc(self):
        pass

    def test_get_all_events_sort_by_creation_time_asc(self):
        pass

    def test_get_all_events_sort_by_creation_time_desc(self):
        pass

    def test_get_all_events_sort_by_popularity_asc(self):
        pass

    def test_get_all_events_sort_by_popularity_desc(self):
        pass

    def test_get_all_events_by_none_location(self):
        pass

    def test_get_all_events_by_non_existing_location(self):
        pass

    def test_get_all_events_by_existing_location(self):
        pass

    def test_post_event(self):
        pass

    def test_post_event_by_unauthorized_user(self):
        pass

    def test_post_event_without_name(self):
        pass

    def test_post_event_without_description(self):
        pass

    def test_post_event_without_date(self):
        pass

    def test_post_event_without_location(self):
        pass


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

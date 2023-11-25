from datetime import timedelta

beat_schedule: dict = {
    'check_events_to_notify': {
        'task': 'app.tasks.event_tasks.check_events_to_notify',
        'schedule': timedelta(minutes=1)
    }
}

from datetime import datetime, timedelta

from celery import chord, group
from flask_mail import Message

from app.database.models.event import Event
from app.mail import mail
from app.tasks import celery, logger
from app.tasks.general_tasks import log_sub_tasks_results


@celery.task
def check_events_to_notify():
    events_to_notify: list[Event] = send_notification.session.query(Event).filter().all()
    sub_tasks = [send_notification.s(event.id) for event in events_to_notify]

    chord(header=group(*sub_tasks), body=log_sub_tasks_results.s(action=check_events_to_notify.name)).delay()

    return True


@celery.task
def send_notification(event_id):
    event = send_notification.session.query(Event).filter(Event.id == event_id).one()

    logger.debug(f'Sending Notification for event #{event.id}')
    msg = Message(subject="Event Reminder",
                  recipients=[participant.email for participant in event.participants])
    msg.body = f"Your event '{event.name}' is happening in 30 minutes!"

    mail.send(msg)

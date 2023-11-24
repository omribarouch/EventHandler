@celery.task
def send_notification(event_id):
    event = get_event_by_id(event_id)

    msg = Message("Event Reminder", recipients=[event.user.email])
    msg.body = f"Your event '{event.name}' is happening in 30 minutes!"

    mail.send(msg)

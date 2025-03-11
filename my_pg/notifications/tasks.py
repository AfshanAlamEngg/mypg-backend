from celery import shared_task
from django.core.mail import send_mail
from .models import Notification, NotificationSettings

@shared_task
def send_email_notification(user_id, subject, message):
    settings = NotificationSettings.objects.get(user_id=user_id)
    if settings.email:
        send_mail(subject, message, 'from@example.com', [settings.user.email])

@shared_task
def send_sms_notification(user_id, message):
    # Integrate with an SMS gateway here
    pass

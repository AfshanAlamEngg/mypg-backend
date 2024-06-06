# from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class NotificationSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.BooleanField(default=True)
    sms = models.BooleanField(default=True)
    in_app = models.BooleanField(default=True)

    def __str__(self):
        return f"Settings for {self.user.username}"

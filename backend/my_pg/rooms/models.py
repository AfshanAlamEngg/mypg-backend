# from django.db import models

# Create your models here.
from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=50)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f'Room {self.room_number}'

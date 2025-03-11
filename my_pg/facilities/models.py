# from django.db import models

# Create your models here.
from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

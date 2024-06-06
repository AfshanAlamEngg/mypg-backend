# from django.db import models

# Create your models here.
from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.TextField()
    properties_owned = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

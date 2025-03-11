# from django.db import models

# Create your models here.
from django.db import models
from tenants.models import Tenant
from staffs.models import Staff

class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('maintenance', 'Maintenance'),
        ('noise', 'Noise'),
        ('cleanliness', 'Cleanliness'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
    ]
    
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    assigned_staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_complaints')
    resolution_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Complaint {self.id} by {self.tenant.name}'

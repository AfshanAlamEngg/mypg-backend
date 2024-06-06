# from django.db import models

# Create your models here.
from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'contact_information', 'created_at', 'updated_at')

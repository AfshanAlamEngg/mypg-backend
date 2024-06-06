# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Owner

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_information', 'properties_owned', 'created_at', 'updated_at')

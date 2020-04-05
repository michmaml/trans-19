from django.contrib import admin
from .models import Patient, Case
from chpstaff.models import Account
# Register your models here.

admin.site.register(Patient)
admin.site.register(Case)
admin.site.register(Account)

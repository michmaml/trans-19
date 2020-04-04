from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(models.Model):
    staff = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    chpStaffNumber = models.CharField(max_length=7)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'{self.staff.first_name} Profile'

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(models.Model):
    #staff = models.ForeignKey(User, on_delete=models.CASCADE)
    chp_staff_number = models.CharField(max_length=7)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name}`s Profile'

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(models.Model):
    #staff = models.ForeignKey(User, on_delete=models.CASCADE)
    chp_staff_number = models.CharField('CHP Staff Number', max_length=7)
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField()
    #epidemiologist = models.BooleanField(default=False)
    username = models.CharField(max_length=30)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField('Re-Enter Your Password', max_length=30)

    def __str__(self):
        return f'{self.first_name}`s Account'

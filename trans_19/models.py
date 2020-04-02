from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DISTRICTS_CHOICES = (
    ('islands', 'ISLANDS'),
    ('kwaitsing', 'KWAI TSING'),
    ('north', 'NORTH'),
    ('saikung', 'SAI KUNG'),
    ('shatin', 'SHA TIN'),
    ('taipo', 'TAI PO'),
    ('tsuenwan', 'TSUEN WAN'),
    ('tuenmun', 'TUEN MUN'),
    ('yuenlong', 'YUEN LONG'),
    ('kowlooncity', 'KOWLOON CITY'),
    ('kwuntong', 'KWUN TONG'),
    ('shamshuipo', 'SHAM SHUI PO'),
    ('wongtaisin', 'WONG TAI SIN'),
    ('yautsimmong', 'YAU TSIM MONG'),
    ('centalwestern', 'CENTRAL & WESTERN'),
    ('eastern', 'EASTERN'),
    ('southern', 'SOUTHERN'),
    ('wanchai', 'WANCHAI')
)

VISIT_CHOICES = (
    ('residence', 'RESIDENCE'),
    ('workplace', 'WORKPLACE'),
    ('visit', 'VISIT'),
    ('other', 'OTHER')
)


class Patient(models.Model):
    name = models.CharField(max_length=30)
    idNum = models.CharField(max_length=10)
    dateBirth = models.DateField()
    dateConfi = models.DateField()
    caseNum = models.IntegerField()


class Case(models.Model):
    nameLocation = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    district = models.CharField(max_length=17, choices=DISTRICTS_CHOICES)
    xCoord = models.IntegerField()
    yCoord = models.IntegerField()
    dateFrom = models.DateField()
    dateTo = models.DateField()
    details = models.CharField(max_length=70)
    category = models.CharField(max_length=9, choices=VISIT_CHOICES)
    patient = models.ForeignKey(Patient, unique=True, on_delete=models.CASCADE)

from django.db import models
from django.urls import reverse

# Create your models here.

DISTRICTS_CHOICES = (
    ('centalwestern', 'Central & Western'),
    ('eastern', 'Eastern'),
    ('islands', 'Islands'),
    ('kowlooncity', 'Kowloon City'),
    ('kwaitsing', 'Kwai Tsing'),
    ('kwuntong', 'Kwun Tong'),
    ('north', 'North'),
    ('saikung', 'Sai Kung'),
    ('shatin', 'Sha Tin'),
    ('shamshuipo', 'Sham Shui Po'),
    ('southern', 'Southern'),
    ('taipo', 'Tai Po'),
    ('tsuenwan', 'Tsuen Wan'),
    ('tuenmun', 'Tuen Mun'),
    ('wanchai', 'Wan Chai'),
    ('wongtaisin', 'Wong Tai Sin'),
    ('yautsimmong', 'Yau Tsim Mong'),
    ('yuenlong', 'Yuen Long')
)

VISIT_CHOICES = (
    ('residence', 'Residence'),
    ('workplace', 'Workplace'),
    ('visit', 'Visit'),
    ('other', 'OTHER')
)


class Patient(models.Model):
    name = models.CharField('Name', max_length=30)
    idNum = models.CharField('ID Number', max_length=10)
    dateBirth = models.DateField('Date of Birth(YYYY-MM-DD)')
    dateConfi = models.DateField('Date of Confirmation(YYYY-MM-DD)')
    caseNum = models.IntegerField('Case Number')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('trans_19_patient', kwargs={'patient': self.pk})

class Location(models.Model):
    name = models.CharField('Location Visited', max_length=70)
    address = models.CharField(max_length=70)
    district = models.CharField(max_length=17, choices=DISTRICTS_CHOICES)
    xCoord = models.IntegerField('X Coordinate')
    yCoord = models.IntegerField('Y Coordinate')
    category = models.CharField(max_length=9, choices=VISIT_CHOICES)

    def __str__(self):
        return self.name

class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    date_From = models.DateField('Date From (YYYY-MM-DD)')
    date_To = models.DateField('Date To (YYYY-MM-DD)')
    details = models.CharField(max_length=70)
    category = models.CharField(max_length=9, choices=VISIT_CHOICES)

    def __str__(self):
        return f'{self.patient} visit - {self.location.name}'

    def get_absolute_url(self):
        return reverse('trans_19_patient', kwargs={'patient': self.patient.id})
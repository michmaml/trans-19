from django.db import models
from django.urls import reverse

# Create your models here.

DISTRICTS_CHOICES = (
    ('Central & Western', 'Central & Western'),
    ('Eastern', 'Eastern'),
    ('Islands', 'Islands'),
    ('Kowloon City', 'Kowloon City'),
    ('Kwai Tsing', 'Kwai Tsing'),
    ('Kwun Tong', 'Kwun Tong'),
    ('North', 'North'),
    ('Sai Kung', 'Sai Kung'),
    ('Sha Tin', 'Sha Tin'),
    ('Sham Shui Po', 'Sham Shui Po'),
    ('Southern', 'Southern'),
    ('Tai Po', 'Tai Po'),
    ('Tsuen Wan', 'Tsuen Wan'),
    ('Tuen Mun', 'Tuen Mun'),
    ('Wan Chai', 'Wan Chai'),
    ('Wong Tai Sin', 'Wong Tai Sin'),
    ('Yau Tsim Mong', 'Yau Tsim Mong'),
    ('Yuen Long', 'Yuen Long')
)

VISIT_CHOICES = (
    ('residence', 'Residence'),
    ('workplace', 'Workplace'),
    ('visit', 'Visit'),
    ('other', 'OTHER')
)

class chp_staff_data(models.Model):
    username = models.CharField('User name', max_length=30)
    chp_staff_number =  models.CharField('chp_staff_number', max_length=30)
    epidemiologist_number =models.CharField('epidemiologist_number', max_length=30)

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
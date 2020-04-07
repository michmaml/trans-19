from django.db import models

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
    name = models.CharField(max_length=30)
    idNum = models.CharField(max_length=10)
    dateBirth = models.DateField()
    dateConfi = models.DateField()
    caseNum = models.IntegerField()

    def __str__(self):
        return self.name


class Case(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name_Location = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    district = models.CharField(max_length=17, choices=DISTRICTS_CHOICES)
    xCoord = models.IntegerField()
    yCoord = models.IntegerField()
    date_From = models.DateField()
    date_To = models.DateField()
    details = models.CharField(max_length=70)
    category = models.CharField(max_length=9, choices=VISIT_CHOICES)

    def __str__(self):
        return f'{self.patient} Case - {self.name_Location}'

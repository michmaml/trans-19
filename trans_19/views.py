from django.shortcuts import render
from .models import Patient

# Create your views here.

'''patients = [
    {
        'name': 'Michal J Sekulski',
        'idNum': 'M9531888',
        'dateBirth': '1999-10-25',
        'dateConfi': '2020-03-31',
        'caseNum': '152'
    },
    {
        'name': 'Zosia Sekulska',
        'idNum': 'Z953NNNN',
        'dateBirth': '2005-09-29',
        'dateConfi': '2020-04-01',
        'caseNum': '111'
    }
]'''


def home(request):
    context = {
        'patients': Patient.objects.all()
    }
    return render(request, 'patients/home.html', context)


def account(request):
    return render(request, 'patients/account.html')

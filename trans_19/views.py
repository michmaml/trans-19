from django.shortcuts import render
from .models import Patient, Case

# Create your views here.


def home(request):
    context = {
        'patients': Patient.objects.all(),
        'trips': Case.objects.all()
    }
    return render(request, 'patients/home.html', context)


def account(request):
    return render(request, 'patients/account.html')

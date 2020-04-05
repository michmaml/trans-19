from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Patient, Case

# Create your views here.


def home(request):
    context = {
        'patients': Patient.objects.all()
    }
    return render(request, 'patients/home.html', context)


class PatientsListView(ListView):
    model = Patient
    template_name = 'patients/home.html'
    context_object_name = 'patients'
    ordering = ['caseNum']


class CaseDetailView(TemplateView):
    #model = Case
    template_name = 'patients/case_detail.html'

    def get_context_data(self, **kwargs):
        patient = self.kwargs['patient']
        context = super().get_context_data(**kwargs)
        context['case_list'] = Case.objects.filter(patient__pk=patient)
        context['patient'] = Patient.objects.get(pk=patient)
        return context


def account(request):
    return render(request, 'patients/account.html')


'''
def trips(request, patient_pk):
    trips = Case.objects.filter(id=patient_pk)
    context = {
        'trips': trips
    }
    return render(request, 'patients/trips.html', context)
'''

'''
class Trips(TemplateView):
    template_name = "trips.html"

    def get_context_data(self, **kwargs):
        patient = self.kwargs['patient']
        context = super().get_context_data(**kwargs)
        context['trips'] = Case.objects.filter(patient__pk=patient)
        context['patient'] = Patient.objects.get(pk=patient)
        return context
'''

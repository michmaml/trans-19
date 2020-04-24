from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, TemplateView, CreateView, UpdateView)
from .models import Patient, Case

# Create your views here.


def home(request):
    context = {
        'patients': Patient.objects.all()
    }
    return render(request, 'patients/home.html', context)


class PatientsListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'patients/home.html'
    context_object_name = 'patients'
    ordering = ['-caseNum']


class CaseDetailView(LoginRequiredMixin, TemplateView):
    #model = Case
    template_name = 'patients/case_detail.html'

    def get_context_data(self, **kwargs):
        patient = self.kwargs['patient']
        context = super().get_context_data(**kwargs)
        context['case_list'] = Case.objects.filter(patient__pk=patient)
        context['patient'] = Patient.objects.get(pk=patient)
        return context


class AddPatientRecordView(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = 'patients/addPatientRecord.html'
    fields = ['name', 'idNum', 'dateBirth', 'dateConfi', 'caseNum']


class UpdatePatientRecordView(LoginRequiredMixin, UpdateView):
    model = Patient
    template_name = 'patients/addPatientRecord.html'
    fields = ['name', 'idNum', 'dateBirth', 'dateConfi', 'caseNum']


def account(request):
    return render(request, 'patients/account.html', {'title': 'Trans-19 Account'})


def view_404(request):
    return render(request, 'patients/page404.html')

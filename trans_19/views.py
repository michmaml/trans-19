from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, TemplateView, CreateView, UpdateView, DeleteView)
from .models import Patient, Visit

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


class PatientDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'patients/patient_trips.html'

    def get_context_data(self, **kwargs):
        patient = self.kwargs['patient']
        context = super().get_context_data(**kwargs)
        context['visit_list'] = Visit.objects.filter(patient__pk=patient)
        context['patient'] = Patient.objects.get(pk=patient)
        return context


class AddPatientRecordView(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = 'patients/patient_actions/add_patient_record.html'
    fields = ['name', 'idNum', 'dateBirth', 'dateConfi', 'caseNum']


class UpdatePatientRecordView(LoginRequiredMixin, UpdateView):
    model = Patient
    template_name = 'patients/patient_actions/update_patient_record.html'
    pk_url_kwarg = 'patient'
    fields = ['name', 'idNum', 'dateBirth', 'dateConfi', 'caseNum']


class DeletePatientRecordView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = 'patients/patient_actions/delete_patient_record.html'
    pk_url_kwarg = 'patient'
    success_url = '/'
    fields = ['name', 'idNum', 'dateBirth', 'dateConfi', 'caseNum']


def account(request):
    return render(request, 'patients/account.html', {'title': 'Trans-19 Account'})


def view_404(request):
    return render(request, 'patients/page404.html')

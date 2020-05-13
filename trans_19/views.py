from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, TemplateView, CreateView, UpdateView, DeleteView)
from .models import Patient, Visit, Location, chp_staff_data
from django import forms
from datetime import datetime, timedelta

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
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        name = self.request.user
        chp_data_list = chp_staff_data.objects.filter(username=name)
        for o in chp_data_list:
            if o.username == name.username:
              context['epidemiologist_number'] = o.epidemiologist_number
              break
        return context


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

    def get_success_url(self, **kwargs):
        return reverse_lazy('trans_19_home')


class UpdatePatientRecordView(LoginRequiredMixin, UpdateView):
    model = Patient
    template_name = 'patients/patient_actions/update_patient_record.html'
    pk_url_kwarg = 'patient'
    success_url = '/'
    fields = ['name', 'idNum', 'dateBirth', 'dateConfi', 'caseNum']


class DeletePatientRecordView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = 'patients/patient_actions/delete_patient_record.html'
    pk_url_kwarg = 'patient'
    success_url = '/'
    fields = ['name', 'idNum', 'dateBirth', 'dateConfi', 'caseNum']


class AddPatientVisitView(LoginRequiredMixin, CreateView):
    model = Visit
    template_name = 'patients/patient_actions/add_patient_visit.html'
    fields = ['location', 'date_From', 'date_To', 'details']

    def form_valid(self, form):
        patient = self.kwargs['patient']
        form.instance.patient = Patient.objects.get(pk=patient)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        patient = self.kwargs['patient']
        context = super().get_context_data(**kwargs)
        context['patientId'] = patient
        return context


class UpdatePatientVisitView(LoginRequiredMixin, UpdateView):
    model = Visit
    template_name = 'patients/patient_actions/update_patient_visit.html'
    pk_url_kwarg = 'visit'
    fields = ['location', 'date_From', 'date_To', 'details']

    def get_context_data(self, **kwargs):
        patient = self.kwargs['patient']
        context = super().get_context_data(**kwargs)
        context['patientId'] = patient
        return context


class DeletePatientVisitView(LoginRequiredMixin, DeleteView):
    model = Visit
    template_name = 'patients/patient_actions/delete_patient_visit.html'
    pk_url_kwarg = 'visit'
    fields = ['location', 'date_From', 'date_To', 'details']

    def get_success_url(self, **kwargs):
        return reverse_lazy('trans_19_patient', kwargs={'patient': self.kwargs['patient']})

    def get_context_data(self, **kwargs):
        patient = self.kwargs['patient']
        context = super().get_context_data(**kwargs)
        context['patientId'] = patient
        success_url = 'patient/' + str(patient)
        return context


class AddLocationRecordView(LoginRequiredMixin, CreateView):
    model = Location
    template_name = 'patients/location_actions/add_location_record.html'
    fields = ['name', 'address', 'district', 'xCoord', 'yCoord', 'category']

    def get_success_url(self, **kwargs):
        return reverse_lazy('trans_19_addLocationRecord')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        return context


class ViewLocationRecordView(LoginRequiredMixin, TemplateView):
    model = Location
    template_name = 'patients/location_actions/location.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('trans_19_location')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        return context


class DeleteLocationView(LoginRequiredMixin, DeleteView):
    model = Location
    pk_url_kwarg = 'location'
    template_name = 'patients/location_actions/delete_location.html'

    def get_success_url(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return reverse_lazy('trans_19_location')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    template_name = 'patients/location_actions/update_location.html'
    pk_url_kwarg = 'location'
    fields = ['name', 'address', 'district', 'xCoord', 'yCoord', 'category']

    def get_success_url(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return reverse_lazy('trans_19_location')


class PatientConnectionsView(LoginRequiredMixin, TemplateView):
    template_name = 'patients/patient_connections.html'

    def get_context_data(self, **kwargs):
        patient_id = self.kwargs['patient']
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=patient_id)

        location_id = - \
            1 if self.request.GET.get('location') == None else int(
                self.request.GET.get('location'))
        time_range = 1 if self.request.GET.get('time_window') == None else int(
            self.request.GET.get('time_window'))

        try:
            case = Patient.objects.get(pk=patient_id)
            visits = Visit.objects.filter(patient=patient_id)
            if location_id != -1:
                visits = visits.filter(location=location_id)
            for visit in visits:
                date_lower_bound = visit.date_From - timedelta(days=time_range)
                date_upper_bound = visit.date_To + timedelta(days=time_range)
                visit.connections = Visit.objects.filter(location=visit.location).filter(
                    date_To__gte=date_lower_bound).filter(date_From__lte=date_upper_bound).exclude(patient_id=patient_id)
        except Patient.DoesNotExist:
            case = None
            visits = None
        except Exception as e:
            visits = None

        context['case'] = case
        context['visits'] = visits

        location_choices = {
            -1: 'All'
        }

        tmp_visits = Visit.objects.filter(patient_id=patient_id)
        for t in tmp_visits:
            location_choices[t.location.id] = t.location.name

        class SearchConnectionForm(forms.Form):
            location = forms.ChoiceField(label='Location', choices=list(
                location_choices.items()), required=True, initial=location_id)
            time_window = forms.IntegerField(
                label='Search window (in days)', required=True, initial=time_range)

        context['form'] = SearchConnectionForm()
        name = self.request.user
        chp_data_list = chp_staff_data.objects.filter(username=name)
        for o in chp_data_list:
            if o.username == name.username:
              context['epidemiologist_number'] = o.epidemiologist_number
              break
        return context


def account(request):
    return render(request, 'patients/account.html', {'title': 'Trans-19 Account'})


def view_404(request):
    return render(request, 'patients/page404.html')

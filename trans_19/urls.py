from django.urls import path
from .views import PatientsListView, PatientDetailView, AddPatientRecordView, UpdatePatientRecordView
from trans_19 import views

urlpatterns = [
    path('', PatientsListView.as_view(), name='trans_19_home'),
    path('patient/<int:patient>/',
         PatientDetailView.as_view(), name='trans_19_patient'),
    path('patient/add/', AddPatientRecordView.as_view(),
         name='trans_19_addPatientRecord'),
    path('patient/<int:patient>/update', UpdatePatientRecordView.as_view(),
         name='trans_19_updatePatientRecord'),
]

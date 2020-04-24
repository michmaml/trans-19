from django.urls import path
from .views import PatientsListView, CaseDetailView, AddPatientRecordView, UpdatePatientRecordView
from trans_19 import views

urlpatterns = [
    path('', PatientsListView.as_view(), name='trans_19_home'),
    path('patient/<int:patient>/',
         CaseDetailView.as_view(), name='trans_19_case'),
    path('patient/add/', AddPatientRecordView.as_view(),
         name='trans_19_addPatientRecord'),
    path('patient/update', UpdatePatientRecordView.as_view(),
         name='trans_19_updatePatientRecord'),
]

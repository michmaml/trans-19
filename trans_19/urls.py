from django.urls import path
from trans_19 import views
from .views import *


urlpatterns = [
    path('', PatientsListView.as_view(),
         name='trans_19_home'),
    path('patient/<int:patient>/', PatientDetailView.as_view(),
         name='trans_19_patient'),
    path('patient/add/', AddPatientRecordView.as_view(),
         name='trans_19_addPatientRecord'),
    path('patient/<int:patient>/visit/add/', AddPatientVisitView.as_view(),
         name='trans_19_addPatientVisit'),
    path('patient/<int:patient>/update/', UpdatePatientRecordView.as_view(),
         name='trans_19_updatePatientRecord'),
    path('patient/<int:patient>/visit/<int:visit>/update/', UpdatePatientVisitView.as_view(),
         name='trans_19_updatePatientVisit'),
    path('patient/<int:patient>/delete/', DeletePatientRecordView.as_view(),
         name='trans_19_deletePatientRecord'),
    path('patient/<int:patient>/visit/<int:visit>/delete/', DeletePatientVisitView.as_view(),
         name='trans_19_deletePatientVisit'),
    path('location/add/', AddLocationRecordView.as_view(),
         name='trans_19_addLocationRecord'),
    path('location/', ViewLocationRecordView.as_view(),
         name='trans_19_location'),
    path('location/location/<int:location>/delete/', DeleteLocationView.as_view(),
         name='trans_19_deleteLocation'),
    path('location/location/<int:location>/update/', UpdateLocationView.as_view(),
         name='trans_19_updateLocation'),
]

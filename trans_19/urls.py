from django.urls import path
from .views import PatientsListView, CaseDetailView
from trans_19 import views

urlpatterns = [
    path('', PatientsListView.as_view(), name='trans_19_home'),
    path('case/<int:patient>/',
         CaseDetailView.as_view(), name='trans_19_case'),
]

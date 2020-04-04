from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='trans_19_home'),
    path('account/', views.account, name='trans_19_account'),
    #path('trips/<int:patients>', views.Trips.as_view(), name='trans_19_trips'),
    path('-<int:patient_pk>/', views.trips, name='trans_19_trips'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='trans_19_home'),
    path('account/', views.account, name='trans_19_account')
]

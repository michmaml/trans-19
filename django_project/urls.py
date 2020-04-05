"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from chpstaff import views as chpstaff_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', chpstaff_views.signup, name='chpstaff_signup'),
    path('account/', chpstaff_views.account, name='chpstaff_account'),
    path('login/', auth_views.LoginView.as_view(template_name='staff/login.html'),
         name='chpstaff_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='staff/logout.html'),
         name='chpstaff_logout'),
    path('', include('trans_19.urls')),
]


'''
<table class="ui celled table" style="text-align: center;">
        <thead>
          <tr>
            <th>Name</th>
            <th>ID Number</th>
            <th>Date of Birth</th>
            <th>Date of Confirmation</th>
            <th>Case Number</th>
          </tr>
        </thead>
        <tbody>
          {% for patient in patients %}
          <tr class='patients' style="cursor:pointer;" onMouseOver="this.style.backgroundColor='rgb(240,240,240)'"
            onMouseOut="this.style.backgroundColor='rgb(255,255,255)'" href="{%url 'trans_19_trips' patient.pk %}">
            <td id='Name'>{{patient.name}}</td>
            <td data-label="ID">{{patient.idNum}}</td>
            <td data-label="Birth">{{patient.dateBirth|date:"d-M-Y"}}</td>
            <td data-label="Confirm">{{patient.dateConfi|date:"d-M-Y"}}</td>
            <td data-label="CaseNum">{{patient.caseNum}}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
'''

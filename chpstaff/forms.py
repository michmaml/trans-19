from django.db.models import IntegerField, Model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# inherits from UserCreationForm


class UserSignInForm(UserCreationForm):
    #CHPStaffNumber = forms.CharField()
    #firstName = forms.CharField()
    #lastName = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
#'CHPStaffNumber', 'firstName', 'lastName',

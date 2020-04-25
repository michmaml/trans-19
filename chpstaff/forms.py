from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from django.forms import HiddenInput

# inherits from UserCreationForm


class UserSignInForm(UserCreationForm):
    chp_staff_number = forms.CharField(max_length=7)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    #epidemiologist = forms.BooleanField(initial=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'chp_staff_number',
                  'email', 'username', 'password1', 'password2']  # , 'epidemiologist'


class UserUpdateAccount(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

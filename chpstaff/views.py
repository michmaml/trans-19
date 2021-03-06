from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSignInForm, UserUpdateAccount
from trans_19.models import chp_staff_data
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if form.is_valid():
            form.save()
            p = chp_staff_data(username = form.cleaned_data.get('username'),chp_staff_number=form.cleaned_data.get('chp_staff_number'), epidemiologist_number = form.cleaned_data.get('epidemiologist_number'))
            p.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created, please log in.')
            return redirect('/login')
    else:
        form = UserSignInForm()
    return render(request, 'staff/signup.html', {'form': form})


@login_required
def account(request):
    if request.method == 'POST':
        form = UserUpdateAccount(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/')
    else:
        form = UserUpdateAccount(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'staff/account.html', context)

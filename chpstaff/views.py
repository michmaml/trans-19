from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignInForm

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('trans_19_home')
    else:
        form = UserSignInForm()
    return render(request, 'staff/signup.html', {'form': form})

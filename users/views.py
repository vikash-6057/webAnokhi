from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('users:home')
        else:
            return render(request, 'users/login.html', {'error': 'Incorrect username or password'})

    else:
        return render(request, 'users/login.html')

@login_required
def home(request):
    return render(request, 'users/home.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


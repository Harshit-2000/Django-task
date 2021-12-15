from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from . import forms
from django.contrib.auth.decorators import login_required
from .models import CustomUser
import requests

# Create your views here.


@login_required(login_url='login')
def home(request):
    response = ''
    if request.method == 'POST':
        url = 'http://127.0.0.1:9000/api/v1/calculate'
        x = request.POST.get('x')
        n = request.POST.get('n')
        data = {
            'x': x,
            'n': n
        }
        response = requests.post(url, json=data)
        response = response.json()

    context = {'response': response}
    return render(request, 'users/home.html', context)


def signupView(request):
    form = forms.SignUpForm()
    message = ''
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phoneNo = form.cleaned_data['phoneNo']
            CustomUser.objects.create_user(
                email=email, password=password, phoneNo=phoneNo)
            return redirect('login')

    context = {'form': form, 'message': message}
    return render(request, 'users/signup.html', context)


def loginView(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            if user:
                login(request, user)
                message = 'Login Successful.'
                return redirect('home')
            else:
                message = 'Login Failed.'

    context = {'form': form, 'message': message}
    return render(request, 'users/login.html', context)


def logoutView(request):
    logout(request)
    return redirect('login')

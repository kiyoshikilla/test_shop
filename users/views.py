from django.shortcuts import render
from users.models import AbstractUser
from users.forms import UserLoginForm, UserRegisterForm 
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
    else:
        form = UserLoginForm()
        
    context = {'form' : form}
    return render(request, 'users/login.html', context)

def register(request):
    context = {'form' : UserRegisterForm}
    return render(request, 'users/register.html', context)
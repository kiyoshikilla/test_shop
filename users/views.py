from django.shortcuts import render
from users.models import AbstractUser
from users.forms import UserLoginForm, UserRegisterForm 

# Create your views here.

def login(request):
    context = {'form' : UserLoginForm}
    return render(request, 'users/login.html', context)

def register(request):
    context = {'form' : UserRegisterForm}
    return render(request, 'users/register.html', context)
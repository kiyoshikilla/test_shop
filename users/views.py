from django.shortcuts import render
from users.models import AbstractUser
from users.forms import UserLoginForm, UserCreationForm 

# Create your views here.

def login(request):
    context = {'form' : UserLoginForm}
    return render(request, 'users/login.html', context)

def register(request):
    context = {'form' : UserCreationForm}
    return render(request, 'users/register.html', context)
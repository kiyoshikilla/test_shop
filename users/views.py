from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm, UserRegisterForm 
from django.contrib import auth, messages

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
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
        
    context = {'form' : form}
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Welcome to our site')
            auth.login(request, user)
            return HttpResponseRedirect(reverse('users:login'))
    else: 
        form = UserRegisterForm()
        
    context = {'form' : form}
    return render(request, 'users/register.html', context)


def profile(request):
 context = {'title' : 'Кабінет'}
 return render(request, 'users/cabinet.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
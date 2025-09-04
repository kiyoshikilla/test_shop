from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=15, required=True)
    last_name = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(max_length=100, required=True)


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
    
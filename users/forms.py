from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from users.models import User

class UserLoginForm(AuthenticationForm):
    pass


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, label="nickname")
    first_name = forms.CharField(max_length=15, required=True)
    last_name = forms.CharField(max_length=15, required=True)


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
    
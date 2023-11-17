from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

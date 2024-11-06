from django.forms import ModelForm
#from .models import Login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'password1', 'password2']

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']
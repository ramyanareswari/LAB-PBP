from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

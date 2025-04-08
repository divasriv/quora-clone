from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    ''' Form for user registration. '''
    class Meta:
        ''' Meta class for RegisterForm. '''
        model = User
        fields = ['username', 'password1', 'password2']

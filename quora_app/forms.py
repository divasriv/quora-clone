from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    ''' Form for creating and updating questions. '''
    class Meta:
        ''' Meta class for QuestionForm. '''
        model = Question
        fields = ['title', 'description']

class AnswerForm(forms.ModelForm):
    ''' Form for creating and updating answers. '''
    class Meta:
        ''' Meta class for AnswerForm. '''
        model = Answer
        fields = ['content']

class RegisterForm(UserCreationForm):
    ''' Form for user registration. '''
    class Meta:
        ''' Meta class for RegisterForm. '''
        model = User
        fields = ['username', 'password1', 'password2']

from django import forms
from django.db import models
from .models import  TaskSteps, TaskPage
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  
from django.db.models.fields import AutoField
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from .models import TaskPage, TaskSteps

class CustomTaskUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskPage
        fields = ['title', 'date', 'description', 'complete']
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }


class StepsForm(forms.ModelForm):
    class Meta:
        model = TaskSteps
        fields = ['body']



class TaskCreateForm(forms.ModelForm):
    required_css_class = 'mt-2'
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "block w-full p-2 text-gray-900 border border-gray-300 rounded-l"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "py-10 px-10 block w-full p-4 text-gray-900 border border-gray-300 rounded-l"}))
    complete = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "my-3 w-4 h-4 text-blue-600 bg-gray-100 border-gray-300"}))

    class Meta:
        model = TaskPage
        fields = ['title', 'date', 'description', 'complete']
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

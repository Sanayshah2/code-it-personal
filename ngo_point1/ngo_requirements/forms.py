from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

class UserForm(UserCreationForm):
    
    email = forms.CharField(max_length=30, label='Email-id')
    first_name = forms.CharField(max_length=20, label='First Name')
    last_name = forms.CharField(max_length=20, label='Last Name')
    
    class Meta:
        model = User
        fields = [ 'first_name','last_name','username','email',  'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password",widget = forms.PasswordInput)


class AddRequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields=['requirement_heading','requirement_content']



    
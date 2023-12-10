from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.CharField(required=True)
    class Meta:
        first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
        last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
        model = User
        fields =['username','first_name','last_name','email']

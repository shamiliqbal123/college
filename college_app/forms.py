
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput
from .models import *





class loginregister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')

class collegeregister(forms.ModelForm):

    class Meta:
        model = college
        fields = ('name','place', 'contact_no', 'e_mail')

class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
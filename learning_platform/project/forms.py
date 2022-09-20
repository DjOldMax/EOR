from django import forms 
from .models import *

class simulator_form(forms.Form):
    text = forms.CharField(max_length=255, label='Поле ввода')

class simulator_form_(forms.Form):
    text = forms.CharField(max_length=255, label='Поле ввода')



from django import forms 
from .models import *

class simulator_form(forms.Form):
    crypt = forms.CharField(max_length=255, label='Поле ввода для зашифровки',required=False)

class simulator_form_(forms.Form):
    decrypt = forms.CharField(max_length=256, label='Поле ввода для расшифровки',required=False)
    privkey = forms.CharField(max_length=256, label='Поле ввода privkey',required=False)

class hash_form(forms.Form):
    hash = forms.CharField(max_length=256, label='Поле ввода:',required=False)

class kuz_encode(forms.Form):
    text = forms.CharField(max_length=256, label='Поле ввода:',required=False)
    pswrd = forms.CharField(max_length=256, label='Поле ввода пороля:',required=False)

class kuz_decode(forms.Form):
    crypto = forms.CharField(max_length=256, label='Поле ввода:',required=False)
    keys = forms.CharField(max_length=256, label='Поле ввода ключей:',required=False)




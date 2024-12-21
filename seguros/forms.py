from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import TextInput
class FormContato(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "w-full mt-1 px-4 py-2 border rounded-md focus:outline-none focus:ring focus:ring-blue-300",
        'placeholder': 'Digite seu Nome'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': "w-full mt-1 px-4 py-2 border rounded-md focus:outline-none focus:ring focus:ring-blue-300",
        'placeholder': 'Digite seu email'
    }))
    
    telefone = PhoneNumberField(region='BR', widget=TextInput(attrs={
        'class': "w-full mt-1 px-4 py-2 border rounded-md focus:outline-none focus:ring focus:ring-blue-300",
        'placeholder': 'Digite seu número'
    }))

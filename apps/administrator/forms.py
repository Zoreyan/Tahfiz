from django import forms
from .models import *


class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ['name', 'phone']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'fullname', 'placeholder': '...'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'id': 'phone', 'placeholder': '996', 'value': '996'})
        }
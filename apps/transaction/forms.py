from django import forms
from .models import *



class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ['amount', 'date', 'semester', 'type']
        widgets = {
            'amount': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'id': 'amount',
                'placeholder': '...',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'date',
                'type': 'date'
            }),
            'semester': forms.Select(attrs={
                'class': 'form-control',
                'id': 'semester',
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
                'id': 'type',
            }),
        }
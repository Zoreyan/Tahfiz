from django import forms
from .models import *



class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['teacher', 'amount', 'total_amount', 'date']

        widgets = {
                'total_amount': forms.TextInput(attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'id': 'total_amount',
                    'placeholder': '...'
                }),
                'amount': forms.TextInput(attrs={
                    'class': 'form-control',
                    'id': 'amount',
                    'type': 'number'
                }),
                'date': forms.TextInput(attrs={
                    'class': 'form-control',
                    'id': 'amount',
                    'type': 'date'
                }),
                'teacher': forms.Select(attrs={
                    'class': 'form-control',
                    'id': 'teacher',
                }),

            }
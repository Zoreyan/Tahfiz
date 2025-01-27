from django import forms
from .models import *
from apps.group.models import Group
from apps.schedule.models import Subject



class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['mark', 'date', 'pages']
        widgets = {
            'mark': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.1}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
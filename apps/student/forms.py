from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'phone', 'group', 'status', 'to_pay', 'image']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'fullname',
                'placeholder': '...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'id': 'image',
                'placeholder': '...'
            }),
            'to_pay': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'id': 'phone',
                'placeholder': '...'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'id': 'phone',
                'placeholder': '...'
            }),
            'group': forms.CheckboxSelectMultiple,
            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'course',
            }),
        }





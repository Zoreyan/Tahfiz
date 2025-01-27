from .models import *
from django import forms

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['title', 'course']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'title',
            }),
            'course': forms.Select(attrs={
                    'class': 'form-control',
                    'id': 'course',
                }),
        }


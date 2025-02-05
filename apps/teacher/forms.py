from django import forms
from .models import *


class TeacherForm(forms.ModelForm):
    """Создание преподавателя"""

    class Meta:
        model = Teacher
        fields = ['name', 'group', 'phone', 'subjects', 'image']
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
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'id': 'phone',
                'placeholder': '...'
            }),

            'subjects': forms.CheckboxSelectMultiple,
            'group': forms.CheckboxSelectMultiple,
        }


class TeacherReportForm(forms.ModelForm):
    class Meta:
        model = TeacherReport
        fields = ['student_quantity', 'total_student_quantity', 'comment']
        widgets = {'comment': forms.TextInput(attrs={'class': 'form-control', 'id': 'comment', 'placeholder': '...'})}


class TeacherCodeForm(forms.Form):
    code = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'code', 'placeholder': '...'}))
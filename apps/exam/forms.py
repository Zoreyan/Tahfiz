from django import forms
from .models import Answer, Exam, Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'pass_points', 'groups']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'pass_points': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            }),
            'groups': forms.CheckboxSelectMultiple,
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']

        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'is_correct': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'customCheckPrimary'
                }),
        }
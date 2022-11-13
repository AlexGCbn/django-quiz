from django import forms
from .models import Category


class QuestionForm(forms.Form):
    DIFF_CHOICES = [
        (None, 'Any'),
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    difficulty = forms.ChoiceField(label='Difficulty', choices=DIFF_CHOICES)
    category = forms.ModelChoiceField(label='Category' ,queryset=Category.objects.all())

    TYPE_CHOICES = [
        ('multiple', 'Multiple Choice'),
        ('boolean', 'True/False'),
    ]
    question_type = forms.ChoiceField(label='Question type', choices=TYPE_CHOICES)

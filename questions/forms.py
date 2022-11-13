from django import forms
from .models import Category


class QuestionForm(forms.Form):
    DIFF_CHOICES = [
        (None, '------'),
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    difficulty = forms.ChoiceField(label='Difficulty', choices=DIFF_CHOICES, required=False)
    category = forms.ModelChoiceField(label='Category' ,queryset=Category.objects.all(), required=False)

    TYPE_CHOICES = [
        (None, '------'),
        ('multiple', 'Multiple Choice'),
        ('boolean', 'True/False'),
    ]
    question_type = forms.ChoiceField(label='Question type', choices=TYPE_CHOICES, required=False)

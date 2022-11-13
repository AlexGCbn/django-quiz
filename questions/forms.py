from django import forms
from .models import Category


class QuestionForm(forms.Form):
    DIFF_CHOICES = [
        (None, 'Any'),
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    difficulty = forms.CharField(label='Difficulty', max_length=50, choices=DIFF_CHOICES)
    category = forms.ModelChoiceField(label='Category' ,queryset=Category.objects.all())

    TYPE_CHOICES = [
        ('multiple', 'Multiple Choice'),
        ('boolean', 'True/False'),
    ]
    question_type = models.CharField(label='Question type', max_length=50, choices=TYPE_CHOICES)

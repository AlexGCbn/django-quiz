from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    name = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024)
    difficulty = models.CharField(max_length=254)
    questions = ArrayField(models.CharField(max_length=254))
    correct_answer = models.CharField(max_length=254)

    TYPE_CHOICES = [
        ('multiple', 'Multiple Choice'),
        ('boolean', 'True/False'),
    ]
    
    question_type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.content

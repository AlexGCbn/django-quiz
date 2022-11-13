from django.contrib import admin
from .models import Category, Question

admin.site.register(Category)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = (
        'category',
        'difficulty', 'question_type'
    )
    list_display = (
        'content', 'category',
        'difficulty', 'question_type'
    )

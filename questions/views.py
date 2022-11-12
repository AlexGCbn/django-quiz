from django.shortcuts import render
from django.views import View
from .models import Category, Question
import random


class HomeView(View):
    # GET request for index/home
    def get(self, request):
        template = 'index.html'
        return render(request, template)


class RandomQuestionsView(View):

    # GET request for random questions game
    def get(self, request):
        template = 'random_question.html'

        question_count = Question.objects.all().count()
        random_question = Question.objects.filter(pk=random.randint(1, question_count))

        context = {
            'question': random_question
        }

        return render(request, template, context)

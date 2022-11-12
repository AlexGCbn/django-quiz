from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Question
from .forms import QuestionForm
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

        form = QuestionForm()
        question_count = Question.objects.all().count()
        random_question = Question.objects.filter(pk=random.randint(1, question_count))

        print(random_question[0].questions)

        context = {
            'question': random_question[0]
        }

        return render(request, template, context)

    def post(self, request):
        template = 'question_result.html'
        
        answer = request.POST['answer']
        q_id = request.POST['question_id']
        result = False

        question = Question.objects.get(id=q_id)
        if question.correct_answer == answer:
            result = True
        
        context = {
            'question': question,
            'answer': answer,
            'result': result,
        }

        return render(request, template, context)
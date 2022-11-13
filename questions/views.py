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
    def get(self, request, difficulty):
        template = 'random_question.html'

        form = QuestionForm()
        question_count = Question.objects.filter(difficulty=difficulty).count()
        diff_questions = Question.objects.filter(difficulty=difficulty)
        rand_question = diff_questions[random.randint(1, question_count)]
        print(rand_question.difficulty)

        context = {
            'question': rand_question,
        }

        return render(request, template, context)

    def post(self, request, difficulty):
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
            'difficulty': difficulty,
        }

        return render(request, template, context)
from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Question
import random


class HomeView(View):

    def get(self, request):
        """GET request for HomeView.
        Displays index page."""
        template = 'index.html'
        return render(request, template)


class RandomQuestionsView(View):

    # GET request for random questions game
    def get(self, request, difficulty, category=None):
        """GET request for RandomQuestionsView.
        Renders a random question based on chosen difficulty."""
        template = 'random_question.html'

        if category:
            question_count = Question.objects.filter(difficulty=difficulty).filter(category=category).count()
            diff_questions = Question.objects.filter(difficulty=difficulty).filter(category=category)
            rand_question = diff_questions[random.randint(0, (question_count - 1))]
            context = {
                'question': rand_question,
                'category_id': category,
            }
        else:
            question_count = Question.objects.filter(difficulty=difficulty).count()
            diff_questions = Question.objects.filter(difficulty=difficulty)
            rand_question = diff_questions[random.randint(0, (question_count - 1))]
            context = {
                'question': rand_question,
            }

        return render(request, template, context)

    # POST request for random questions
    # handles
    def post(self, request, difficulty, category=None):
        """POST request for RandomQuestionsView.
        Handles the form POST method to get question and check if answer is correct.
        Renders a result page."""
        template = 'question_result.html'
        
        answer = request.POST['answer']
        q_id = request.POST['question_id']
        result = False

        question = Question.objects.get(id=q_id)
        if question.correct_answer == answer:
            result = True

        # Check if category_id exists to pass in context
        category_id = request.POST['category_id'] if 'category_id' in request.POST else None
        
        context = {
            'question': question,
            'answer': answer,
            'result': result,
            'difficulty': difficulty,
            'category_id': category_id,
        }

        return render(request, template, context)


class CategoriesView(View):

    def get(self, request):
        """GET request for CategoriesView.
        Renders a page to display categories for user to pick."""
        template = 'categories.html'

        categories = Category.objects.all()

        context = {
            'categories': categories,
        }

        return render(request, template, context)

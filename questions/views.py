from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Question
from .forms import QuestionForm
import random


class QuestionFormView(View):

    def get(self, request):
        template = 'index.html'
        form = QuestionForm()
        context = {
            'form': form,
        }

        return render(request, template, context)



class RandomQuestionsView(View):

    # GET request for random questions game
    def get(self, request):
        """GET request for RandomQuestionsView.
        Renders a random question based on chosen difficulty."""
        template = 'random_question.html'

        no_question = False
        rand_question = []
        # Handle questions with form
        form = QuestionForm(request.GET)
        if form.is_valid():
            difficulty = form.cleaned_data['difficulty']
            category = form.cleaned_data['category'].id if form.cleaned_data['category'] else None
            question_type = form.cleaned_data['question_type']

        # Conditional filters
        difficulty_filter = {'difficulty': difficulty} if difficulty else {}
        category_filter = {'category': category} if category else {}
        question_type_filter = {'question_type': question_type} if question_type else {}
        print(difficulty_filter)
        print(category_filter)
        print(question_type_filter)

        # Get question count and choose a random question
        question_count = Question.objects.filter(**difficulty_filter).filter(**category_filter).filter(**question_type_filter).count()
        diff_questions = Question.objects.filter(**difficulty_filter).filter(**category_filter).filter(**question_type_filter)
        try:
            rand_question = diff_questions[random.randint(0, (question_count - 1))]
        except:
            no_question = True
        context = {
            'question': rand_question,
            'difficulty': difficulty,
            'category': category,
            'question_type': question_type,
            'no_question': no_question,
        }

        return render(request, template, context)

    # POST request for random questions
    # handles
    def post(self, request):
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

        # Check if any game options exist to pass in context
        difficulty = request.POST['difficulty'] if 'difficulty' in request.POST else None
        category = request.POST['category'] if 'category' in request.POST else None
        question_type = request.POST['question_type'] if 'question_type' in request.POST else None
        
        context = {
            'question': question,
            'answer': answer,
            'result': result,
            'difficulty': difficulty,
            'category': category,
            'question_type': question_type,
        }

        return render(request, template, context)

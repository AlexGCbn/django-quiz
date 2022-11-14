from django.test import TestCase
from .models import Category, Question
from .forms import QuestionForm
from . import views
from django.test.client import RequestFactory 


class TestViews(TestCase):

    def setUp(self):
        """
        Set up function to create test objects
        """

        self.factory = RequestFactory()

        test_category = Category.objects.create(
            name="Test category"
        )

        test_question = Question.objects.create(
            category=test_category,
            content="Test question",
            difficulty="easy",
            answers=["answer1", "answer2", "answer3"],
            correct_answer="answer1",
            question_type="multiple"
        )

    def test_question_form_view(self):
        """
        Test home page
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_random_question_no_form(self):
        """
        Test random question without form data
        """
        response = self.client.get('/random/')
        self.assertEqual(response.status_code, 200)

    def test_random_question_no_question(self):
        """
        Test random question in case of no question found
        Also tests QuestionForm
        """
        category = Category.objects.get(id=1)
        data = {'difficulty': 'medium', 'category': 1, 'question_type': 'boolean'}
        form = QuestionForm({'difficulty': 'medium', 'category': category, 'question_type': 'boolean'})
        response = self.client.get('/random/', data)
        self.assertTrue(form.is_valid())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['no_question'])

    def test_random_question_post(self):
        """
        Test random question POST method
        """
        # Test correct answer
        response = self.client.post('/random/', {
            'question_id': 1,
            'answer': 'answer1',
            'difficulty': 'easy',
            'category': 1,
            'question_type': 'multiple'
            })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['result'])
        # Test incorrect answer
        response = self.client.post('/random/', {
            'question_id': 1,
            'answer': 'answer2',
            'difficulty': 'easy',
            'category': 1,
            'question_type': 'multiple'
            })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['result'])

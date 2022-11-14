from django.test import TestCase
from .models import Category, Question


class TestModels(TestCase):

    def setUp(self):
        """
        Set up function to create test objects
        """

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

    def test_category_str(self):
        """
        Test if category was created successfully.
        """
        category = Category.objects.get(id=1)
        category_str = str(category)
        self.assertEqual(category_str, "Test category")

    def test_question_str(self):
        """
        Test if category was created successfully.
        """
        question = Question.objects.get(id=1)
        question_str = str(question)
        self.assertEqual(question_str, "Test question")
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
            category=1,
            content="Test question",
            difficulty="easy",
            answers=["answer1", "answer2", "answer3"],
            correct_answer="answer1",
            question_type="multiple"
        )

    def test_category_creation(self):
        """
        Test if category was created successfully.
        """
        category = Category.objects.get(id=1)
        self.assertEqual(category.name, "Test category")
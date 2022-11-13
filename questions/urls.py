from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionFormView.as_view(), name='home'),
    path('random/', views.RandomQuestionsView.as_view(), name='random_question'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('random/<str:difficulty>', views.RandomQuestionsView.as_view(), name='random_question'),
]
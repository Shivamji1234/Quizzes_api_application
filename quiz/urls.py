from django.urls import path
from .views import create_quiz, get_active_quiz, get_quiz_result, get_all_quizzes


urlpatterns = [
    path("quizzes/",create_quiz,name="quiz-list-created"),
    path("quizzes/active/",get_active_quiz,name="active-quiz"),
    path("quizzes/<int:id>/Result/",get_quiz_result,name="quiz-result"),
    path("quizzes/all/",get_all_quizzes,name="quiz-list")
]
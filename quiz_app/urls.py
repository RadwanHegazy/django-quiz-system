from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add-quiz/',views.add_quiz,name='add_quiz'),
    path('add-quiz/questions/<str:quizuuid>/',views.add_quiz_questions,name='add_quiz_questions'),
    path('quiz/enter/<str:quizuuid>/',views.user_enter_exam,name='enter_quiz'),
    path('check/',views.save_answers,name='check'),
    path('quiz-result/<str:answeruuid>/',views.quiz_result,name='result'),
    path('all-quiz/',views.all_quiz,name='all_quiz'),
    path('quiz-answers/',views.get_quiz_answers,name='quiz_answers'),
]
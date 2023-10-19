from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add-quiz/',views.add_quiz,name='add_quiz'),
    path('add-quiz/questions/<str:quizuuid>/',views.add_quiz_questions,name='add_quiz_questions'),
    path('quiz/enter/<str:quizuuid>/',views.user_enter_exam,name='enter_quiz'),
    path('check/',views.save_answers,name='check'),
]
from django.contrib import admin
from .models import Question, Quiz, Answer, Student



class QuizBoard (admin.ModelAdmin) :
    list_display = ['title','user']

admin.site.register(Quiz,QuizBoard)


class QuestionBoard (admin.ModelAdmin) :
    list_display = ['q','quiz']

admin.site.register(Question, QuestionBoard)


class AnswerBoard (admin.ModelAdmin) :
    list_display = ['full_name','quiz']

admin.site.register(Answer, AnswerBoard)

admin.site.register(Student)
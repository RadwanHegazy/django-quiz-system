from django.contrib import admin
from .models import Question, Quiz


class QuizBoard (admin.ModelAdmin) :
    list_display = ['title','user']

admin.site.register(Quiz,QuizBoard)


class QuestionBoard (admin.ModelAdmin) :
    list_display = ['q','quiz']

admin.site.register(Question, QuestionBoard)

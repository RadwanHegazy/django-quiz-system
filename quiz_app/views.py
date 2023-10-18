from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question

@login_required
def home (request) :
    return render(request,'main/home.html')


@login_required
def add_quiz (request) :

    user = request.user

    if request.method == "POST" : 
        q = Quiz.objects.create(
            title = request.POST['title'],
            time = request.POST['time'],
            user = user,
        )

        return redirect('add_quiz_questions', q.uuid)

    return render(request,'main/add-quiz.html')


@login_required
def add_quiz_questions (request, quizuuid) : 

    quiz = get_object_or_404(Quiz, uuid=quizuuid)

    if quiz.user != request.user : 
        return HttpResponseForbidden(request)
    
    context = {
        'qs_count' : Question.objects.filter(quiz = quiz).count(),
        'quiz' : quiz,
    }

    if request.method == "POST" : 
        
        state = request.POST['state']

        if state == 'add' :
            q = Question.objects.create(
                quiz = quiz,
                q = request.POST['q'],
                a_1 = request.POST['a_1'],
                a_2 = request.POST['a_2'],
                a_3 = request.POST['a_3'],
                a_4 = request.POST['a_4'],
                correct_answer = request.POST['correct_answer']
            )

            return redirect('add_quiz_questions', quizuuid)
        
        elif state == 'finish' : 
            return redirect('home')
        
        
    return render(request,'main/add-quiz-questions.html', context)
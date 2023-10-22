from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Answer, Student
import ast, json

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


def user_enter_exam (request, quizuuid) : 
    
    quiz = get_object_or_404(Quiz,uuid=quizuuid)
    context = {
        'quiz' : quiz,
    }

    if request.method == "POST" :
        full_name = request.POST['full_name']



        st = Answer.objects.create(
            full_name = full_name,
            quiz = quiz
        )

        if 'picture' in request.FILES : 
            st.image = request.FILES['picture']

        st.save()

        context['student_uuid'] = str(st.uuid) 

        return render(request,'main/questions.html',context)
    
    
    if 'api' in request.GET :
        data = [ {'uuid' : str(i.uuid),'q_title' : i.q,'a_1' : i.a_1,'a_2' : i.a_2,'a_3' : i.a_3,'a_4' : i.a_4}  for i in Question.objects.filter(quiz=quiz)]
        return JsonResponse(data,safe=False)
    
    return render(request,'main/enter-quiz.html',context)



def save_answers (request) :

    if request.method == "GET" : 
        return HttpResponseForbidden(request)

    st_uuid = request.POST['student_uuid']
    answer = Answer.objects.get(uuid=st_uuid)

    quiz_uuid = request.POST['quiz_uuid']
    quiz = Quiz.objects.get(uuid=quiz_uuid)


    user_answers = ast.literal_eval(request.POST['answers'])


    user_result = 0
    total_mark = Question.objects.filter(quiz=quiz).count()


    for i in user_answers :
        q = Question.objects.get(uuid=i['question_uuid'])

        if q.correct_answer == i['user_answer'] : 
            user_result += 1
    

    answer.mark = f"{user_result} / {total_mark}"
    answer.save()


    done_url = redirect('result',answer.uuid)
    return HttpResponse(done_url.url)


def quiz_result (request, answeruuid) : 
    answer = get_object_or_404(Answer,uuid=answeruuid)

    return render(request,'main/result.html',{'answer':answer})
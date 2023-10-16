from django.shortcuts import redirect
from users_app.models import User
from django.http import HttpResponseNotAllowed
from django.contrib.auth.views import auth_login
from django.contrib import messages


def login (request) : 
    if request.method == "POST" :
        data = {
            'email' : request.POST['email'],
            'password' : request.POST['password'],
        }
        user = User.login(**data)

        if user['errors'] :
            error = user['errors']
            messages.info(request,error)

            return redirect('user_auth')

        user = user['user']
        auth_login(request,user=user)
        return redirect('home')
        
    
    else:
        return HttpResponseNotAllowed(request)
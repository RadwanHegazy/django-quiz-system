from django.shortcuts import redirect
from django.http import HttpResponseNotAllowed
from users_app.models import User
from django.contrib.auth.views import auth_login

def register (request) : 
    if request.method == "POST" :
        data = {
            'email' : request.POST['email'],
            'password' : request.POST['password'],
            'full_name' : request.POST['full_name'],
        }
        user = User.objects.create_user(**data)

        if 'picture' in request.FILES :
            user.picture = request.FILES['picture']

        user.save()

        auth_login(request,user=user)
        return redirect('home')
        
    
    else:
        return HttpResponseNotAllowed(request)
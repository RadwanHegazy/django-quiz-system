from django.shortcuts import HttpResponse, render




def view_auth_template (request) : 
    return render(request,'auth/auth.html')
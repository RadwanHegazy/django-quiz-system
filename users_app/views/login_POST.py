from django.shortcuts import HttpResponse


def login (request) : 
    if request.method == "POST" :
        return HttpResponse('Home Template')
    else:
        return HttpResponse('Method Not Allowed')
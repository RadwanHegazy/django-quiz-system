from django.shortcuts import HttpResponse


def register (request) : 
    if request.method == "POST" :
        return HttpResponse('Home Template')
    else:
        return HttpResponse('Method Not Allowed')
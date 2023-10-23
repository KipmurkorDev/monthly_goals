from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):

    if (request.method == 'GET'):
        return HttpResponse("Hello here are my all blog")
    if (request.method == 'POST'):
        return HttpResponse("Hello here are my all blog")
    if (request.method == 'PUT'):
        return HttpResponse("Hello here are my all blog")
    if (request.method == 'DELETE'):
        return HttpResponse("Hello here are my all blog")

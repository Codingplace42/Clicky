from django.shortcuts import render
from django.http.response import HttpResponse


def click(request):
    return HttpResponse("Hello")

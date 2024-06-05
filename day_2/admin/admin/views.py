from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("hello, Home page!")


def about(request):
    return HttpResponse("hello, about page!")


def contact(request):
    return HttpResponse("hello, contact page!")

def htmlPage(request):
    return render(request, 'index.html')
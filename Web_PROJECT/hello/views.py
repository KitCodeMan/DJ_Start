from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello,world. you're at the polls index.")

def amir(request):
    return HttpResponse("Hello,amir")

def akbar(request):
    return HttpResponse("Hello,akbar")

def greet(request,name):
    return HttpResponse(f"Hello,{name}")
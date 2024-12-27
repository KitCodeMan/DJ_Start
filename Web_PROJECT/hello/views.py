from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'hello/index.html')

def amir(request):
    return HttpResponse("Hello,amir")

def akbar(request):
    return HttpResponse("Hello,akbar")

def greet(request,name):
    return HttpResponse(f"<h1> Hello,{name}</h1>")
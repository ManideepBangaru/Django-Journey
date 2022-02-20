from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("<h1>Hello Manoj !!!, I'm Django</h1>")

def home(request):
    return render(request, "home.html",{'name':'Shravani'})

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    addvalue = val1 + val2
    return render(request, "result.html", {'result': addvalue, "val1" : val1, "val2":val2})
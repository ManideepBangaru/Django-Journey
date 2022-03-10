from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def Greet(request):
#     return HttpResponse("<h1> Hello World !!! </h1>")

def Home(request):
    return render(request,"Home.html")

def Add(request):
    val1 = int(request.GET['Num1'])
    val2 = int(request.GET['Num2'])
    addvalue = val1 + val2
    return render(request,"result.html",{"result":addvalue})
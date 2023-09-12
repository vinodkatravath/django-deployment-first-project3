from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1(request):
    return HttpResponse("<h1>hello from Demoapp1 f1() </h1><hr/>")
def f2(request):
    return HttpResponse("<h2>hello from Demoapp2 f2() </h2><hr/>")
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "mrb/index.html")
    
def index(request):
    return HttpResponse("Momentum Ojrdus!")

def kex(request):
    return HttpResponse("mrb kex box >:D")

def penes(request):
    return HttpResponse("Penes reisimiz Penes babamız <3")

def greet(request, name):
    return render(request, "mrb/greet.html", {
        "name": name.capitalize()
    })

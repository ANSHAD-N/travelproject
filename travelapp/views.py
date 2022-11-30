from django.http import HttpResponse
from django.shortcuts import render
from . models import Destinations

# Create your views here.


def demo(request):
    destinations = Destinations.objects.all()
    return render(request, 'index.html', {'place': destinations})


def about(request):
    return render(request, "about.html")


def contacts(request):
    return HttpResponse("hello world")


def addition(request):
    x = int(request.GET['input1'])
    y = int(request.GET['input2'])
    res = x+y
    return render(request ,"result.html", {'result':res})

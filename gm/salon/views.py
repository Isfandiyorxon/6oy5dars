from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from .models import Cars,Brend

def home(request:WSGIRequest):
    brends=Brend.objects.all()
    return render(request,'brends.html',{'brends':brends})

def moshinalar(request:WSGIRequest):
    cars=Cars.objects.all()
    return render(request,'cars.html',{'cars':cars})


# Create your views here.

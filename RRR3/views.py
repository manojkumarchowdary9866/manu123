from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rc(request):
    return HttpResponse('<marquee><h1> one of the indain biggest actor and one of my favourate actor </h1><marquee>')

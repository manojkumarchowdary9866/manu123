from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ss(request):
    return HttpResponse('<marquee><h1> indain biggest blockbuster never before ever after</h1><marquee>')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ntr(request):
    return HttpResponse('<marquee><h1> indain biggest actor and my favourate actor </h1><marquee>')

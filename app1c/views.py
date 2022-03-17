from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def manojc(request):
    return HttpResponse('<marquee><h1>waiting for rrr movie</h1><marquee>')

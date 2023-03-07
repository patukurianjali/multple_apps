from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_first(request):
    return HttpResponse('<h1> IT is first view function app2</h2>')
def app2_second(request):
    return HttpResponse('<h1> IT is second view function app2</h2>')
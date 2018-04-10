from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, how are you?")

# Create your views here.

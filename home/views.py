from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.


def index(request):
    return HttpResponse("raiffeisen bank index page.")

def login(request):
    return render_to_response('home/login.html')
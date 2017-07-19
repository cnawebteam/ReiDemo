from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def index(request):
    return render_to_response('home/index.html')


def login(request):
    return render_to_response('home/login.html')


def users(request):
    return render_to_response('home/users.html')


def campaigns(request):
    return render_to_response('home/campaigns.html')


def transactions(request):
    return render_to_response('home/transactions.html')

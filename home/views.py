from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf


def index(request):
    return render_to_response('home/index.html')


def login(request):
    return render_to_response('home/login.html')


def users(request):
    return render_to_response('home/users.html')


def campaigns(request):
    return render_to_response('home/campaigns.html')


def campaign_details(request, campaign_id=None):
    if campaign_id is None:
        raise Http404("Campaign does not exist")

    args = {}
    args.update(csrf(request))

    args['campaign_id'] = campaign_id

    return render_to_response('home/campaign_details.html', args)


def transactions(request):
    return render_to_response('home/transactions.html')

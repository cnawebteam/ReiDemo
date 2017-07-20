from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from home.forms import EditCampaignForm
from django.core.urlresolvers import reverse
import json


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

    mock_json = {"parent_category": "red", "category": "Charity", "description": "This is the descr","status": "inactive"}

    if request.method == 'POST':
            form = EditCampaignForm(request.POST, initial={'parent_category': mock_json['parent_category'],
                                                           'category': mock_json['category'],
                                                           'description': mock_json['description'],
                                                           'status': mock_json['status']})
            if form.is_valid():
                return HttpResponseRedirect(reverse('index'))
    else:
        form = EditCampaignForm(initial={'parent_category': mock_json['parent_category'],
                                         'category': mock_json['category'],
                                         'description': mock_json['description'],
                                         'status': mock_json['status']})

    args['form'] = form

    return render_to_response('home/campaign_details.html', args)


def transactions(request):
    return render_to_response('home/transactions.html')

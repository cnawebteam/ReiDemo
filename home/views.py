import requests, json
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from home.forms import EditCampaignForm
from django.core.urlresolvers import reverse


def index_view(request):
    try:
        response = requests.get('https://ct-campaign-service.herokuapp.com/campaignProposal')
        content = response.content

        my_json = content.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
    except:
        data = "Could not fetch Campaign Proposals"

    args = {}
    args.update(csrf(request))

    args['content'] = data

    return render_to_response('home/index.html', args)


def home_redirect(response):
    return HttpResponseRedirect(reverse('home'))


def login(request):
    return render_to_response('home/login.html')


def users(request):
    try:
        response = requests.get('https://ct-campaign-service.herokuapp.com/person')
        content = response.content

        my_json = content.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
    except:
        data = "Could not fetch Users"

    args = {}
    args.update(csrf(request))

    args['content'] = data

    return render_to_response('home/users.html', args)


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
            return HttpResponseRedirect(reverse('campaigns'))
    else:
        form = EditCampaignForm(initial={'parent_category': mock_json['parent_category'],
                                         'category': mock_json['category'],
                                         'description': mock_json['description'],
                                         'status': mock_json['status']})

    args['form'] = form

    return render_to_response('home/campaign_details.html', args)


def campaign_proposals(request, proposal_id=None):
    args = {}
    args.update(csrf(request))

    args['proposal_id'] = proposal_id

    mock_json = {"parent_category": "red", "category": "Charity", "description": "This is the descr","status": "inactive"}

    if request.method == 'POST':
        form = EditCampaignForm(request.POST, initial={'parent_category': mock_json['parent_category'],
                                                       'category': mock_json['category'],
                                                       'description': mock_json['description'],
                                                       'status': mock_json['status']})
        if form.is_valid():
            return HttpResponseRedirect(reverse('campaigns'))
    else:
        form = EditCampaignForm(initial={'parent_category': mock_json['parent_category'],
                                         'category': mock_json['category'],
                                         'description': mock_json['description'],
                                         'status': mock_json['status']})

    args['form'] = form

    return render_to_response('home/campaign_proposal.html', args)


def transactions(request):
    r = requests.get('http://httpbin.org/get')

    args = {}
    args.update(csrf(request))

    args['status'] = r.status_code

    return render_to_response('home/transactions.html', args)

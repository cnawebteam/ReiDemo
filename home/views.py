import requests, json
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from home.forms import EditCampaignForm, EditProposalForm
from django.core.urlresolvers import reverse


def home_redirect(response):
    return HttpResponseRedirect(reverse('home'))


def login_view(request):
    return render_to_response('home/login.html')


def users_view(request):
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


def campaign_proposals_view(request):
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

    return render_to_response('home/campaign_proposals.html', args)


def campaign_proposal_details_view(request, proposal_id=None):
    try:
        response = requests.get('https://ct-campaign-service.herokuapp.com/campaignProposal/' + proposal_id)
        content = response.content

        my_json = content.decode('utf8').replace("'", '"')
        json_data = json.loads(my_json)
    except:
        raise Http404("Campaign proposal does not exist")

    args = {}
    args.update(csrf(request))

    args['proposal_id'] = proposal_id

    if request.method == 'POST':
        form = EditProposalForm(request.POST, initial={'campaign_url': json_data['campaignUrl'],
                                                       'description': json_data['description'],
                                                       'status': json_data['proposalStatus']})
        if form.is_valid():

            json_data['campaignUrl'] = form.cleaned_data['campaign_url']
            json_data['description'] = form.cleaned_data['description']
            json_data['proposalStatus'] = form.cleaned_data['status']
            try:
                headers = {"Content-Type": "application/json"}
                r = requests.put('https://ct-campaign-service.herokuapp.com/campaignProposal/' + proposal_id,
                                 headers=headers,
                                 data=json.dumps(json_data))
            except:
                raise Http404("Campaign does not exist")
            return HttpResponseRedirect(reverse('home:proposals'))
    else:
        form = EditProposalForm(initial={'campaign_url': json_data['campaignUrl'],
                                         'description': json_data['description'],
                                         'status': json_data['proposalStatus']})

    args['form'] = form

    return render_to_response('home/campaign_proposal_details.html', args)


def campaigns_view(request):
    try:
        response = requests.get('https://ct-campaign-service.herokuapp.com/campaign')
        content = response.content

        my_json = content.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
    except:
        data = "Could not fetch Campaigns"

    args = {}
    args.update(csrf(request))

    args['content'] = data

    return render_to_response('home/campaigns.html', args)


def campaign_details_view(request, campaign_id=None):
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
            return HttpResponseRedirect(reverse('home:campaigns'))
    else:
        form = EditCampaignForm(initial={'parent_category': mock_json['parent_category'],
                                         'category': mock_json['category'],
                                         'description': mock_json['description'],
                                         'status': mock_json['status']})

    args['form'] = form

    return render_to_response('home/campaign_details.html', args)


def transactions_view(request):
    r = requests.get('http://httpbin.org/get')

    args = {}
    args.update(csrf(request))

    args['status'] = r.status_code

    return render_to_response('home/transactions.html', args)

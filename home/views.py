from graphos.renderers import morris
from graphos.sources.model import ModelDataSource
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart
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
    data = [
       ['Pending', 'Running', 'Failed', 'Finished'],
       ['Pending', 100],
       ['Running', 40],
       ['Failed', 3],
       ['Finished', 10],
    ]
    data_source = SimpleDataSource(data=data)
    chart = morris.DonutChart(data_source, height=250, width=250)

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
    args['chart'] = chart

    return render_to_response('home/campaign_proposals.html', args)


def campaign_proposal_details_view(request, proposal_id=None):
    try:
        response = requests.get('https://ct-campaign-service.herokuapp.com/campaignProposal/' + proposal_id)
        content = response.content

        my_json = content.decode('utf8')
        json_data = json.loads(my_json)
    except:
        raise Http404("Campaign proposal does not exist")

    args = {}
    args.update(csrf(request))

    args['proposal_id'] = proposal_id

    initial_data = {'campaign_type': json_data['campaignType'],
                    'permanent_residence': json_data['initiator']['permanentResidence'],
                    'email': json_data['initiator']['email'],
                    'mobile_number': json_data['initiator']['mobileNumber'],
                    'project_location': json_data['projectLocation'],
                    'IBAN': json_data['initiator']['iban'],
                    'campaign_page_url': json_data['campaignUrl'],
                    'campaign_page_id': json_data['campaignPageId'],
                    'description': json_data['description'],
                    'comments': json_data['description'],
                    'status': json_data['proposalStatus'],
    }

    if request.method == 'POST':
        form = EditProposalForm(request.POST, initial=initial_data)
        if form.is_valid():
            # json_data['campaignType'] = form.cleaned_data['campaign_category']
            # json_data['initiator']['permanentResidence'] = form.cleaned_data['permanent_residence']
            # json_data['initiator']['email'] = form.cleaned_data['email']
            # json_data['initiator']['mobileNumber'] = form.cleaned_data['mobile_number']
            # json_data['projectLocation'] = form.cleaned_data['project_location']
            # json_data['initiator']['iban'] = form.cleaned_data['IBAN']
            # json_data['campaignUrl'] = form.cleaned_data['campaign_page_url']
            # json_data['campaignPageId'] = form.cleaned_data['campaign_page_id']
            # json_data['description'] = form.cleaned_data['description']
            # json_data['campaignUrl'] = form.cleaned_data['comments']
            json_data['proposalStatus'] = form.cleaned_data['status']
            headers = {"Content-Type": "application/json"}
            r = requests.put('https://ct-campaign-service.herokuapp.com/campaignProposal/' + proposal_id,
                             headers=headers,
                             data=json.dumps(json_data))
            if form.cleaned_data['status'] == 'APPROVED':
                r = requests.post('https://ct-campaign-service.herokuapp.com/campaignProposal/' + proposal_id + '/start',
                                  headers=headers)
            return HttpResponseRedirect(reverse('home:proposals'))
    else:
        form = EditProposalForm(initial=initial_data)

    args['form'] = form
    args['data'] = json_data

    return render_to_response('home/campaign_proposal_details.html', args)


def campaigns_view(request):
    try:
        response = requests.get('https://ct-campaign-service.herokuapp.com/campaign')
        content = response.content

        my_json = content.decode('utf8')
        data = json.loads(my_json)
    except:
        data = "Could not fetch Campaigns"

    args = {}
    args.update(csrf(request))

    args['content'] = data

    return render_to_response('home/campaigns.html', args)


def campaign_details_view(request, campaign_id=None):
    try:
        response = requests.get('https://ct-campaign-service.herokuapp.com/campaign/' + campaign_id)
        content = response.content

        my_json = content.decode('utf8').replace("'", '"')
        json_data = json.loads(my_json)
    except:
        raise Http404("Campaign  does not exist")

    args = {}
    args.update(csrf(request))

    args['campaign_id'] = campaign_id

    initial_data = {'campaign_type': "test",
                    'permanent_residence': json_data['owner']['permanentResidence'],
                    'email': json_data['owner']['email'],
                    'mobile_number': json_data['owner']['mobileNumber'],
                    # 'project_location': json_data['projectLocation'],
                    'IBAN': json_data['owner']['iban'],
                    'campaign_page_url': json_data['campaignUrl'],
                    # 'campaign_page_id': json_data['campaignPageId'],
                    # 'description': json_data['description'],
                    # 'comments': json_data['description'],
                    'status': json_data['campaignStatus'],
    }

    if request.method == 'POST':
        form = EditCampaignForm(request.POST, initial=initial_data)
        if form.is_valid():
            return HttpResponseRedirect(reverse('home:campaigns'))
    else:
        form = EditCampaignForm(initial=initial_data)

    args['form'] = form

    return render_to_response('home/campaign_details.html', args)


def transactions_view(request):
    r = requests.get('http://httpbin.org/get')

    args = {}
    args.update(csrf(request))

    args['status'] = r.status_code

    return render_to_response('home/transactions.html', args)

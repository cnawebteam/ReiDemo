from graphos.renderers import morris, gchart
from graphos.sources.model import ModelDataSource
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart, PieChart
import requests, json
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from home.forms import EditCampaignForm, EditProposalForm, EditProposalFormApproved
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
        json_data = json.loads(my_json)
    except:
        json_data = "Could not fetch Users"

    args = {}
    args.update(csrf(request))

    args['content'] = json_data

    return render_to_response('home/users.html', args)


def campaign_proposals_view(request):
    chart_data = [
       ['Running', 'Pending', 'Failed', 'Finished'],
       ['Running', 101],
       ['Pending', 40],
       ['Failed', 3],
       ['Finished', 10],
    ]
    # data_source = SimpleDataSource(data=chart_data,)
    # chart = morris.DonutChart(data_source, height=250, width=250)
    # chart = morris.DonutChart(data_source, html_id='donut_div')

    try:
        response = requests.get('https://ct-campaign-service.herokuapp.com/campaignProposal')
        content = response.content

        my_json = content.decode('utf8').replace("'", '"')
        json_data = json.loads(my_json)
    except:
        json_data = "Could not fetch Campaign Proposals"

    args = {}
    args.update(csrf(request))

    args['content'] = json_data
    # args['chart'] = chart
    args['chart_data'] = chart_data

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
                    'comments': json_data['approverDetails'],
                    'status': json_data['proposalStatus'],
    }

    if request.method == 'POST':
        if json_data['proposalStatus'] == 'Approved':
            form = EditProposalFormApproved(request.POST, initial=initial_data)
        else:
            form = EditProposalForm(request.POST, initial=initial_data)

        headers = {"Content-Type": "application/json"}
        if form.is_valid():
            json_data['campaignType'] = form.cleaned_data['campaign_type']
            json_data['projectLocation'] = form.cleaned_data['project_location']
            json_data['campaignUrl'] = form.cleaned_data['campaign_page_url']
            json_data['campaignPageId'] = form.cleaned_data['campaign_page_id']
            json_data['description'] = form.cleaned_data['description']
            json_data['proposalStatus'] = form.cleaned_data['status']
            json_data['approverDetails'] = form.cleaned_data['comments']

            r = requests.put('https://ct-campaign-service.herokuapp.com/campaignProposal/' + proposal_id,
                             headers=headers,
                             data=json.dumps(json_data))

            if form.cleaned_data['status'] == 'Approved' and request.POST.get("start_campaign"):
                r = requests.post('https://ct-campaign-service.herokuapp.com/campaignProposal/' + proposal_id + '/start',
                                  headers=headers)
                campaign_id = json.loads(r.content.decode('utf8'))['id']
                return HttpResponseRedirect(reverse('home:campaign_details', kwargs={'campaign_id': campaign_id}))
            else:
                return HttpResponseRedirect(reverse('home:campaign_proposal_details', kwargs={'proposal_id': proposal_id}))
    else:
        if json_data['proposalStatus'] == 'Approved':
            form = EditProposalFormApproved(initial=initial_data)
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
        json_data = json.loads(my_json)

        for entry in json_data:
            if entry['currentAmount'] is not None and entry['targetAmount'] is not None:
                current = (entry['currentAmount']) = 20000
                target = (entry['targetAmount'])
                # current = (20000)
                value = ((current / target) * 100)
                entry['progress'] = round(value, 2)
    except:
        json_data = "Could not fetch Campaigns"

    args = {}
    args.update(csrf(request))

    args['content'] = json_data

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
                    'description': json_data['description'],
                    'comments': json_data['comment'],
                    'status': json_data['campaignStatus'],
    }

    if request.method == 'POST':
        form = EditCampaignForm(request.POST, initial=initial_data)
        if form.is_valid():
            return HttpResponseRedirect(reverse('home:campaigns'))
    else:
        form = EditCampaignForm(initial=initial_data)

    args['form'] = form
    args['data'] = json_data

    return render_to_response('home/campaign_details.html', args)


def transactions_view(request):
    try:
        response = requests.get('https://ct-campaign-service.herokuapp.com/campaignPledge/')
        content = response.content

        my_json = content.decode('utf8')
        json_data = json.loads(my_json)
    except:
        raise Http404("Cannot fetch transactions")

    args = {}
    args.update(csrf(request))

    args['content'] = json_data

    return render_to_response('home/transactions.html', args)

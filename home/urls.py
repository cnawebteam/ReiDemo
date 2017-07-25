from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_redirect, name='index'),
    url(r'^users/$', views.users_view, name='users'),
    url(r'^campaigns/$', views.campaigns_view, name='campaigns'),
    url(r'^campaign_proposals/$', views.campaign_proposals_view, name='proposals'),
    url(r'^transactions/$', views.transactions_view, name='transactions'),
    url(r'^campaigns/(?P<campaign_id>\d+)/$', views.campaign_details_view, name='campaign_details'),
    url(r'^campaign_proposals/(?P<proposal_id>\d+)/$', views.campaign_proposal_details_view, name='campaign_proposal_details'),
]

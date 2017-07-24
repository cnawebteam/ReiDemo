from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_redirect, name='index'),
    url(r'^users/$', views.users, name='users'),
    url(r'^campaigns/$', views.campaigns, name='campaigns'),
    url(r'^campaign_proposals/$', views.campaign_proposals, name='proposals'),
    url(r'^transactions/$', views.transactions, name='transactions'),
    url(r'^campaigns/(?P<campaign_id>\d+)/$', views.campaign_details, name='campaign_details'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^users/$', views.users, name='users'),
    url(r'^campaigns/$', views.campaigns, name='campaigns'),
    url(r'^transactions/$', views.transactions, name='transactions'),
    url(r'^campaigns/(?P<campaign_id>\d+)/$', views.campaign_details, name='campaign_details'),
]

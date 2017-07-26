from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.layout import Layout, Div
from django import forms

from django import forms
from crispy_forms.helper import FormHelper

CAMPAIGN_STATUSES = (
    ('PENDING', 'PENDING'),
    ('RUNNING', 'RUNNING'),
    ('FINISHED', 'FINISHED'),
    ('FAILED', 'FAILED')
)

PROPOSAL_STATUSES = (
    ('PENDING', 'PENDING'),
    ('APPROVED', 'APPROVED'),
    ('REJECTED', 'REJECTED')
)


class EditCampaignForm(forms.Form):
    helper = FormHelper()
    helper.form_tag = False

    parent_category = forms.ChoiceField(label='Product category', choices=CAMPAIGN_STATUSES)
    category = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    status = forms.ChoiceField(label='Status', choices=CAMPAIGN_STATUSES)


class EditProposalForm(forms.Form):
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div('campaign_category', css_class='col-sm-6',),
            Div('project_location', css_class='col-sm-6',),
            Div('permanent_residence', css_class='col-sm-6',),
            Div('email', css_class='col-sm-6',),
            Div('mobile_number', css_class='col-sm-6',),
            Div('IBAN', css_class='col-sm-6',),
            Div('campaign_page_url', css_class='col-sm-6',),
            Div('campaign_page_id', css_class='col-sm-6',),
            Div('description', css_class='col-sm-6',),
            Div('comments', css_class='col-sm-6',),
            Div('status', css_class='col-sm-12',),
        ),
    )

    campaign_category = forms.CharField(max_length=100)
    permanent_residence = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    mobile_number = forms.CharField(max_length=100)
    project_location = forms.CharField(max_length=100)
    IBAN = forms.CharField(max_length=100)
    campaign_page_url = forms.URLField(required=True)
    campaign_page_id = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    comments = forms.CharField(widget=forms.Textarea, label="Approver Comments")
    status = forms.ChoiceField(label='Status', choices=PROPOSAL_STATUSES)

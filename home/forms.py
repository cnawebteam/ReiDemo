from crispy_forms.layout import Layout, Div

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

PROPOSAL_TYPE = (
    ('CHARITY', 'CHARITY'),
    ('SPORTS', 'SPORTS'),
    ('TECHNOLOGY', 'TECHNOLOGY'),
    ('ART', 'ART'),
    ('ANIMALS', 'ANIMALS'),
    ('CULTURE', 'CULTURE'),
    ('COMMUNITY_PROJECTS', 'COMMUNITY_PROJECTS'),
)

helper_layout = Layout(Div(
        Div('campaign_type', css_class='col-sm-6',),
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


class EditCampaignForm(forms.Form):
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(Div(
        Div('campaign_type', css_class='col-sm-6',),
        # Div('project_location', css_class='col-sm-6',),
        Div('permanent_residence', css_class='col-sm-6',),
        Div('email', css_class='col-sm-6',),
        Div('mobile_number', css_class='col-sm-6',),
        Div('IBAN', css_class='col-sm-6',),
        Div('campaign_page_url', css_class='col-sm-6',),
        # Div('campaign_page_id', css_class='col-sm-6',),
        # Div('description', css_class='col-sm-6',),
        # Div('comments', css_class='col-sm-6',),
        Div('status', css_class='col-sm-12',),
    ),
)

    campaign_type = forms.CharField(max_length=100, disabled=True)
    permanent_residence = forms.CharField(max_length=100, disabled=True)
    email = forms.EmailField(max_length=100, disabled=True)
    mobile_number = forms.CharField(max_length=100, disabled=True)
    # project_location = forms.CharField(max_length=100, disabled=True)
    IBAN = forms.CharField(max_length=100, disabled=True)
    campaign_page_url = forms.CharField(max_length=100, disabled=True)
    # campaign_page_id = forms.CharField(max_length=100, disabled=True)
    # description = forms.CharField(widget=forms.Textarea, disabled=True)
    # comments = forms.CharField(widget=forms.Textarea, label="Approver Comments", disabled=True)
    status = forms.ChoiceField(label='Status', choices=PROPOSAL_STATUSES, disabled=True)


class EditProposalForm(forms.Form):
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(Div(
        Div('campaign_type', css_class='col-sm-6',),
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

    campaign_type = forms.ChoiceField(label='Type', choices=PROPOSAL_TYPE)
    permanent_residence = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    mobile_number = forms.CharField(max_length=100)
    project_location = forms.CharField(max_length=100)
    IBAN = forms.CharField(max_length=100)
    campaign_page_url = forms.CharField(max_length=100)
    campaign_page_id = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    comments = forms.CharField(widget=forms.Textarea, label="Approver Comments")
    status = forms.ChoiceField(label='Status', choices=PROPOSAL_STATUSES)

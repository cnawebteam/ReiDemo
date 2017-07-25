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

    campaign_url = forms.URLField(required=True)
    description = forms.CharField(widget=forms.Textarea)
    status = forms.ChoiceField(label='Status', choices=PROPOSAL_STATUSES)

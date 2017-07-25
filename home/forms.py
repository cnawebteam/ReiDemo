from django import forms

from django import forms
from crispy_forms.helper import FormHelper

COLOR_CHOICES = (
    ('PENDING','PENDING'),
    ('RUNNING', 'RUNNING'),
    ('APPROVED','APPROVED'),
    ('REJECTED','REJECTED'),
    )

CAMPAIGN_STATUSES = (('ACTIVE','ACTIVE'),
                     ('INACTIVE', 'INACTIVE'),
                     ('ASDASD', 'ASDASD')
                     )


class EditCampaignForm(forms.Form):
    helper = FormHelper()
    helper.form_tag = False

    parent_category = forms.ChoiceField(label='Product category', choices=COLOR_CHOICES)
    category = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    status = forms.ChoiceField(label='Status', choices=CAMPAIGN_STATUSES)
    # image


class EditProposalForm(forms.Form):
    helper = FormHelper()
    helper.form_tag = False

    # parent_category = forms.ChoiceField(label='Product category', choices=COLOR_CHOICES)
    campaign_url = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    status = forms.ChoiceField(label='Status', choices=CAMPAIGN_STATUSES)
    # image


from django import forms

from django import forms
from crispy_forms.helper import FormHelper

COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)


class EditCampaignForm(forms.Form):
    helper = FormHelper()
    helper.form_tag = False

    parent_category = forms.ChoiceField(label='Product category', choices=COLOR_CHOICES)
    category = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    status = forms.ChoiceField(label='Status', choices=(('active','ACTIVE'), ('inactive', 'INACTIVE')))
    # image
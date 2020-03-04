from django.forms import forms

class SearchForm(forms.Form):
    sub_reddit = forms.Field(label='Sub-reddit name')

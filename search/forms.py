from django import forms
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from cms.models import Page

class SearchForm(forms.Form):
	query	= forms.CharField()

        def search(self):
		return  Page.objects.search(self.cleaned_data['query'])

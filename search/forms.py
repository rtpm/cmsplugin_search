from django import forms
from cms.models import Page

class SearchForm(forms.Form):
	query	= forms.CharField()

        def search(self):
		return  Page.objects.search(self.cleaned_data['query'])

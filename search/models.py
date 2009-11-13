from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin

class Search(CMSPlugin):
	search_label 	= models.CharField(_('Search field label'), max_length=100)
	submit 	= models.CharField(_('Submit title'), max_length=100)
	found 	= models.CharField(_('Found title'), max_length=100)
	not_found = models.CharField(_('Not found label'), max_length=100)
	more	= models.CharField(_('More text'), max_length=200)

	def __unicode__(self):
		return self.found

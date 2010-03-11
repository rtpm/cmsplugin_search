from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Search
from forms import SearchForm

class SearchPlugin(CMSPluginBase):
    model = Search
    name = _("Search Form")
    render_template = "search.html"
    
    def render(self, context, instance, placeholder):
	request = context['request']

	if request.GET.get('query', None) is not None:
		form = SearchForm(request.GET)
		if form.is_valid():
			results = form.search()
			context.update( {
				'search': instance,
				'results': results,
				'query': request.GET['query'],
				'form': form,
				})
			return context
	else:
		form = SearchForm()

	
        context.update({
		'search': instance,
		'form': form,
        	})
        return context
    
plugin_pool.register_plugin(SearchPlugin)

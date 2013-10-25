from django.conf.urls.defaults import *
from waguwagu.search import *

urlpatterns = patterns('',
		(r'^$', main_views.main_page),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'c:\\project\\waguwagu\\images'}), 
    (r'^search/(?P<mode>[a-z,A-Z]+)/(?P<keyword>\S+)/Page(?P<page>\d+)/$', search_views.BlogSearchPage),
    (r'^search/(?P<mode>[a-z,A-Z]+)/(?P<keyword>\S+)/$', search_views.BlogSearchPage),
) 

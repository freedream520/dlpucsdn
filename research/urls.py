from django.conf.urls import patterns, include, url

urlpatterns = patterns('research.views',
    url(r'^$','research_index',name='research_index'),
)
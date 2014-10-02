from django.conf.urls import patterns, include, url
from forum.views import create_topic

urlpatterns = patterns('forum.views',
    url(r'^$','topic_list',name='forum'),
    url(r'^create/$','create_topic'),
)
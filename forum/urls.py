from django.conf.urls import patterns, include, url
from forum.views import create_topic

urlpatterns = patterns('forum.views',
    url(r'^create/$','create_topic',name='create_topic'),
    url(r'^(?P<topic_id>\d+)/$','topic_view',name='topic_view'),
    url(r'^(?P<topic_id>\d+)/reply$','create_reply',name='create_reply'),
    url(r'^(?P<topic_id>\d+)/delete$','del_topic',name='del_topic'),
)
from django.conf.urls import patterns, include, url
from account.views import *

urlpatterns = patterns('account.views',
    url(r'^(?P<user_id>\d+)/$','user_profile',name='user_profile'),
)
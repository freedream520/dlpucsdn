from django.conf.urls import patterns, include, url
from account.views import *

urlpatterns = patterns('account.views',
    url(r'^index','index'),
)
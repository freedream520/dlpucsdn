from django.conf.urls import patterns, include, url

urlpatterns = patterns('home.views',
    url(r'^$', 'home'),
)
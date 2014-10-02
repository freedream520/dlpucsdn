from django.conf.urls import patterns, include, url

urlpatterns = patterns('assignment.views',
    url(r'^$','assignment_main',name='assignment'),
    url(r'^issue/$','assignment_issue',name='issue')
)
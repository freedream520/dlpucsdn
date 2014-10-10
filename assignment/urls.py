from django.conf.urls import patterns, include, url

urlpatterns = patterns('assignment.views',
    url(r'^$','assignment_index',name='assignment_index'),
    url(r'^issue/$','assignment_issue',name='issue')
)
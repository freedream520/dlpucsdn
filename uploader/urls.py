from django.conf.urls import patterns, include, url

urlpatterns = patterns('uploader.views',
    # url(r'^$','index'),
    url(r'^$','src_index',name='src_index'),
)
from django.conf.urls import patterns, include, url

urlpatterns = patterns('uploader.views',
    url(r'^$','src_index',name='src_index'),
    url(r'^upload/$','upload_file',name='upload_file'),
    url(r'^receive/$','receive_url',name='receive_url'),
)
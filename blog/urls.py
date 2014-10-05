from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^write/$','write_blog',name='write_blog'),
)
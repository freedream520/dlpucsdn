from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$','blog_list',name='blog'),
    url(r'^write/$','write_blog',name='write'),
)
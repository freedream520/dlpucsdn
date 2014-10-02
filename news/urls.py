from django.conf.urls import patterns, include, url

urlpatterns = patterns('news.views',
    url(r'^$','news_list',name='news'),
    url(r'add/$','add_news'),
)
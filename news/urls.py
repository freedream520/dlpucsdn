from django.conf.urls import patterns, include, url

urlpatterns = patterns('news.views',
    url(r'add/$','add_news',name='add_news'),
    url(r'$','news_index',name='news_index'),
)
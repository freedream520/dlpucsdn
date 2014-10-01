from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','account.views.index'),
    url(r'^$','news.views.news_view'),
    url(r'^index/$','account.views.index'),
    url(r'^login/$','account.views.user_login'),
    url(r'^signup/$','account.views.user_signup'),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout


urlpatterns = patterns('',
    # Examples:
    url(r'^$','account.views.index',name='index'),
    url(r'^index/','account.views.index',name='index'),
    url(r'^login/','account.views.user_login'),
    url(r'^signup/','account.views.user_signup'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^forum/',include('forum.urls')),
    url(r'^news/',include('news.urls')),
    url(r'^blog/',include('blog.urls')),
    url(r'^assignment/',include('assignment.urls')),
    url(r'^about/$','account.views.about',name='about'),
    url(r'^research/',include('research.urls')),
)

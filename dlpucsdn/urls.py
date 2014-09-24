from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dlpucsdn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',include('home.urls')),
    url(r'^login/$','account.views.user_signup'),
    url(r'^signup/$','account.views.user_signup'),
    url(r'^admin/', include(admin.site.urls)),
)

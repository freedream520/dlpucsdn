from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout


urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'account.views.index', name='index'),
                       url(r'^index/', 'account.views.index', name='index'),
                       url(r'^login/', 'account.views.user_login', name='login'),
                       url(r'^logout/', 'account.views.user_logout', name='logout'),
                       url(r'^signup/', 'account.views.user_signup', name='signup'),
                       url(r'^about/$', 'account.views.about', name='about'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^assignment/', include('assignment.urls')),
                       url(r'^user/',include('account.urls')),
                       url(r'^(?P<dn>\w+)/research/', include('research.urls')),
                       url(r'^(?P<dn>\w+)/blog/', include('blog.urls')),
                       url(r'^(?P<dn>\w+)/forum/', include('forum.urls')),
                       url(r'^(?P<dn>\w+)/', include('news.urls')),
                       url(r'^(?P<dn>\w+)/forum/$', 'forum.views.forum_index', name='forum_index'),
                       url(r'^(?P<dn>\w+)/blog/$', 'blog.views.blog_index', name='blog_index'),
                       url(r'^(?P<dn>\w+)/research/$', 'research.views.research_index', name='research_index'),

)

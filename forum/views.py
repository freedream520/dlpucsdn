from django.shortcuts import render,render_to_response,RequestContext
from account.models import department
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forum.models import topic
from django.template import RequestContext
from forum.models import topic

# Create your views here.

def create_topic(request,dn):
    d = department.objects.get(name = dn)
    if request.method == 'GET':
        return render_to_response('forum/create.html',{'user':request.user,
                                                       'dn':dn,
                                                       'department':d.cn},
                                  context_instance = RequestContext(request))
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        t = topic()
        t.department_name = d
        t.title = title
        t.content = content
        t.auth = request.user
        t.save()
    return HttpResponseRedirect(reverse('forum_index',kwargs={'dn':dn}))


def forum_index(request,dn):
    d = department.objects.get(name = dn)
    t = topic()
    t.department_name = d
    topics = topic.objects.filter(department_name = d)
    return render_to_response('forum/index.html',{'dn':dn,
                                                  'user':request.user,
                                                  'topics':topics,
                                                  'department':d.cn},
                              context_instance = RequestContext(request))

def topic_view(request,dn,topic_id):
    d = department.objects.get(name = dn)
    t = topic.objects.get(id = topic_id)
    return render_to_response('forum/topic.html',{'user':request.user,
                                                  'dn':dn,
                                                  'department':d.cn,
                                                  'topics':t})
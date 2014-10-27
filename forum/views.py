#coding=utf-8
from django.shortcuts import render, render_to_response, RequestContext
from account.models import department
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forum.models import topic
from django.template import RequestContext
from forum.models import topic, reply
from datetime import datetime
from django.contrib import messages
from django.utils.translation import ugettext as _
import re
from django.contrib.auth.models import User
from forum.models import mention
# Create your views here.

def create_topic(request, dn):
    d = department.objects.get(name=dn)
    if request.method == 'GET':
        return render_to_response('forum/create.html', {'user': request.user,
                                                        'dn': dn,
                                                        'title':u'创建一个主题',
                                                        'department': d.cn},
                                  context_instance=RequestContext(request))
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        if not title:
            messages.add_message(request,messages.WARNING,_(u'标题不能为空'))
            return HttpResponseRedirect(reverse('create_topic',kwargs={'dn':dn}))
        t = topic()
        t.department_name = d
        t.title = title
        t.content = content
        t.auth = request.user
        t.save()
    return HttpResponseRedirect(reverse('forum_index', kwargs={'dn': dn}))


def forum_index(request, dn):
    d = department.objects.get(name=dn)
    t = topic()
    t.department_name = d
    topics = topic.objects.filter(department_name=d,deleted = False)
    return render_to_response('forum/index.html', {'dn': dn,
                                                   'user': request.user,
                                                   'title':u'主题列表',
                                                   'topics': topics,
                                                   'department': d.cn},
                              context_instance=RequestContext(request))


def topic_view(request, dn, topic_id):
    d = department.objects.get(name=dn)
    t = topic.objects.get(id=topic_id)
    r = reply.objects.filter(topic=topic_id)
    t.click += 1
    t.save()
    return render_to_response('forum/topic.html', {'user': request.user,
                                                   'dn': dn,
                                                   'department': d.cn,
                                                   'reply': r,
                                                   'title': t.title,
                                                   'request':request,
                                                   'topic_id': topic_id,
                                                   'topics': t},
                              context_instance=RequestContext(request))


def create_reply(request, dn, topic_id):
    if request.method == 'POST':
        d = department.objects.get(name=dn)
        t = topic.objects.get(id=topic_id)
        r = reply()
        r.auth = request.user
        r.topic = t
        r.content = request.POST['reply']
        r.save()
        t.click -=1
        t.last_replied = datetime.now()
        t.reply_count +=1
        t.save()
        return HttpResponseRedirect(reverse('topic_view',kwargs={'topic_id':topic_id,
                                                                 'dn':dn}))

def del_topic(request, dn, topic_id):
    t = topic.objects.get(id = topic_id)
    if request.user == t.auth:
        t.deleted = True
        t.save()
        messages.add_message(request,messages.WARNING,_(u'删除成功！'))
    else:
        messages.add_message(request,messages.WARNING,_(u'删除失败，你不是这个主题的作者！'))
    return HttpResponseRedirect(reverse('forum_index',kwargs={'dn':dn}))
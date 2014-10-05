from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from news.models import list
from account.models import department
from django.core.urlresolvers import reverse

def add_news(request,dn):
    d = department.objects.get(name = dn)
    if request.method == 'GET':
        return render_to_response('news/add.html',{'user':request.user,
                                                   'dn':dn,
                                                   'department':d.cn},
                                  context_instance = RequestContext(request))
    elif request.method == 'POST':
        n = list()
        title = request.POST['title']
        url = request.POST['url']
        auth = request.user
        if title and url:
            n.title = title
            n.url = url
            n.auth = auth
            n.department_name = d
            n.save()
        else:
            return HttpResponse('blank')
    return HttpResponseRedirect(reverse('news_index',kwargs={'dn':dn}))

def news_index(request,dn):
    if department.objects.filter(name = dn).exists():
        d = department.objects.get(name = dn)
        new = list()
        new.department_name = d
        news = list.objects.filter(department_name = d)
        return render_to_response('news/list.html',{'user':request.user,
                                                    'dn':dn,
                                                    'news':news,
                                                    'department':d.cn},
                                  context_instance = RequestContext(request))



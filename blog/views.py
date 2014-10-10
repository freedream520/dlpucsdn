from django.shortcuts import render,render_to_response,RequestContext
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from account.models import department
from blog.models import blogs,breply
from django.core.urlresolvers import reverse
from django.template import RequestContext
# Create your views here.

def write_blog(request,dn):
    d = department.objects.get(name = dn)
    if request.method == 'GET':
        return render_to_response('blog/write.html',{'user':request.user,
                                              'dn':dn,
                                              'department':d.cn},
                                  context_instance = RequestContext(request))
    elif request.method == 'POST':
        b = blogs()
        b.auth = request.user
        b.title = request.POST['title']
        b.content = request.POST['content']
        b.department_name = d
        b.save()
        return HttpResponseRedirect(reverse('blog_index',kwargs={'dn':dn}))

def blog_view(request,dn,blog_id):
    d = department.objects.get(name=dn)
    b = blogs.objects.get(id=blog_id)
    b.click += 1
    b.save()
    br = breply.objects.filter(topic=blog_id)
    return render_to_response('blog/view.html',{'user':request.user,
                                                'blog':b,
                                                'request':request,
                                                'dn':dn,
                                                'breply':br,
                                                'blog_id':blog_id,
                                                'department':d.cn},
                             context_instance = RequestContext(request))


def blog_index(request,dn):
    d = department.objects.get(name = dn)
    blog = blogs.objects.filter(department_name = d,deleted = False)
    return render_to_response('blog/index.html',{'dn':dn,
                                                 'blog':blog,
                                                 'user':request.user,
                                                 'department':d.cn},
                              context_instance = RequestContext(request))

def create_breply(request,dn,blog_id):
    if request.method == 'POST':
        b = blogs.objects.get(id = blog_id)
        br = breply()
        br.auth = request.user
        br.content = request.POST['content']
        br.topic = b
        br.save()
        b.click -=1
        b.reply_count +=1
        b.save()
        return HttpResponseRedirect(reverse('blog_view',kwargs={'dn':dn,
                                                                'blog_id':blog_id}))
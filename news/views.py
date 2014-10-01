from django.shortcuts import render
from News.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

# Create your views here.
def news_add(request):
    if request.method=='GET':
        url = request.POST['url']
        title = request.POST['title']
        auth = request.user
        n = News()
        click = n.click+1
        n.click = click
        n.url = url
        n.title = title
        n.auth = auth
        n.save()
        return render_to_response('index.html',
                                  context_instance=RequestContext(request))
    return HttpResponseRedirect('index')
def news_view(request):
    n = News()
    click = n.click
    title = n.title
    url = n.url
    auth = n.auth
    news = {'url':url,'title':title,'auth':auth,'click':click}
    return render_to_response('index.html',{'news':news})
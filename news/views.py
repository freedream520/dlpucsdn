from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from news.models import news

# Create your views here.
def news_list(request):
    return render_to_response('news/list.html')

def add_news(request):
    return render_to_response('news/add.html')
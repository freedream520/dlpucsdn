#coding=utf-8
from django.shortcuts import render,render_to_response
from account.models import department
# Create your views here.

def research_index(request,dn):
    d = department.objects.get(name = dn)
    return render_to_response('research/index.html',{'dn':dn,
                                                     'title':u'%s--科研'%(d.cn),
                                                     'department':d.cn,
                                                     'user':request.user})
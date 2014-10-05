from django.shortcuts import render,render_to_response
from account.models import department
# Create your views here.

def write_blog(request,dn):
    d = department.objects.get(name = dn)
    return render_to_response('blog/write.html',{'user':request.user,
                                                 'dn':dn,
                                                 'department':d.cn})

def blog_index(request,dn):
    d = department.objects.get(name = dn)
    return render_to_response('blog/index.html',{'dn':dn,
                                                 'user':request.user,
                                                 'department':d.cn})
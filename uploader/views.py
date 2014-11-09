#coding=utf-8
from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from uploader.models import files
from django.contrib import messages
from django.utils.translation import ugettext as _
import sys
import qiniu.conf
import qiniu.rs
import qiniu.io
import json
import base64

qiniu.conf.ACCESS_KEY="vco8VEaZwm24oxn9btpSdjVUMGUe21-K049IlIbl"
qiniu.conf.SECRET_KEY="jTUDwXmbx8uzSG-jEXAfigbQN8Aj3Q3-K6eDU6Ru"

def upload_file(request):
    file = qiniu.rs.PutPolicy('dlpucsdn')
    file.returnUrl = "http://127.0.0.1:8000/src/receive"
    token = file.token()
    extra = qiniu.io.PutExtra()
    extra.mime_type = "text/plain"
    extra.params = {'x:title': 'description'}
    return render_to_response('uploader/upload.html',{'token':token,
                                                      'user':request.user,
                                                   'request':request},
                              context_instance = RequestContext(request))

def receive_url(request):
    if request.method == 'GET':
        ret = request.GET['upload_ret']
        if ret:
            lens = len(ret)
            lenx = lens - (lens % 4 if lens % 4 else 4)
            try:
                fileInfo = json.loads(base64.decodestring(ret))
            except:
                messages.add_message(request,messages.WARNING,u'上传出错，请尝试缩短文件描述')
                return HttpResponseRedirect(reverse('upload_file'))
            key = fileInfo['key']
            title = fileInfo['x:title']
            if title:
                domain = 'dlpucsdn.qiniudn.com'
                base_url = qiniu.rs.make_base_url(domain, key)
                policy = qiniu.rs.GetPolicy()
                private_url = policy.make_request(base_url)  # 获得下载地址
                f = files()
                f.auth = request.user
                f.title = title
                f.url = private_url
                f.save()
                messages.add_message(request,messages.WARNING,u'上传成功！')
                return HttpResponseRedirect(reverse('src_index',))
            messages.add_message(request,messages.WARNING,_(u'文件的描述不能为空！'))
            return HttpResponseRedirect(reverse('upload_file'))
        return render_to_response('uploader/error.html')
    return render_to_response('uploader/error.html')

def src_index(request):
    file = files.objects.all()
    return render_to_response('uploader/src.html',{'file':file,
                                                   'request':request},
                              context_instance = RequestContext(request))
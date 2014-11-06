#coding=utf-8
from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from uploader.models import files
from django.contrib import messages
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
    key = 'view'
    if request.method == 'POST':
        f = files.objects.get(auth =request.user)
        title = request.POST['title']
        f.auth = request.user
        f.title = title
        f.save()
        file = files.objects.get()
        local_file = '%s'%__file__
        ret,err = qiniu.io.put_file(token,key,local_file)
        if err is not None:
            sys.stderr.write('%s'%err)
        messages.add_message(request,messages.WARNING,u'上传成功')
    return render_to_response('uploader/upload.html',{'token':token,
                                                   'request':request},
                              context_instance = RequestContext(request))

def receive_url(request):
    if request.method == 'GET':
        ret = request.GET['upload_ret']
        if ret:
            fileInfo = json.loads(base64.decodestring(ret))
            key = fileInfo['key']
            domain = 'dlpucsdn.qiniudn.com'
            base_url = qiniu.rs.make_base_url(domain, key)
            policy = qiniu.rs.GetPolicy()
            private_url = policy.make_request(base_url)  # 获得下载地址
            return HttpResponseRedirect(reverse('src_index',kwargs={'request':request}))
        return render_to_response('uploader/error.html')
    return render_to_response('uploader/error.html')

def src_index(request):
    file = files.objects.all()
    return render_to_response('uploader/src.html',{'file':file})
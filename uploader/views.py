#coding=utf-8
from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
import sys
import qiniu.conf
import qiniu.rs
import qiniu.io
import json
import base64
qiniu.conf.ACCESS_KEY="vco8VEaZwm24oxn9btpSdjVUMGUe21-K049IlIbl"
qiniu.conf.SECRET_KEY="jTUDwXmbx8uzSG-jEXAfigbQN8Aj3Q3-K6eDU6Ru"

def src_index(request):
    file = qiniu.rs.PutPolicy('dlpucsdn')
    file.returnUrl = "http://127.0.0.1:8000/src"
    token = file.token()
    key = 'view'
    if request.method == 'POST':
        local_file = '%s'%__file__
        ret,err = qiniu.io.put_file(token,key,local_file)
        if err is not None:
            sys.stderr.write('%s'%err)
    return render_to_response('uploader/src.html',{'token':token,
                                                   'request':request},
                              context_instance = RequestContext(request))
#coding=utf-8
from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
import json
import base64
import ssl
import qiniu.conf
import qiniu.rs
import qiniu.io
import sys

qiniu.conf.ACCESS_KEY="vco8VEaZwm24oxn9btpSdjVUMGUe21-K049IlIbl"
qiniu.conf.SECRET_KEY="jTUDwXmbx8uzSG-jEXAfigbQN8Aj3Q3-K6eDU6Ru"

import qiniu.resumable_io as rio



def src_index(request):
    policy = qiniu.rs.PutPolicy("dlpucsdn")
    uptoken = policy.token()
    if request.method=="GET":
        return render_to_response('uploader/src.html',{'request':request,
                                                       'token':uptoken},
                                  context_instance=RequestContext(request))
    elif request.method=="POST":
        f = request.POST['image']
        ret, err = qiniu.io.put_file(uptoken, f,)
        if err is not None:
            sys.stderr.write('error: %s ' % err)
            return
        return HttpResponseRedirect(reverse('src_index',kwargs={'request':request}),
                                    context_instance=RequestContext(request))

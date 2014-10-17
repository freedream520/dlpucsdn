#coding=utf-8
from django.shortcuts import render,render_to_response
import qiniu.io
import qiniu.rs
# Create your views here.
def src_index(request):
    return render_to_response('uploader/src.html')
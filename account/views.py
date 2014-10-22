# coding=utf-8
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from account.models import profile
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.core.mail import send_mail, mail_admins
import base64
import re
# Create your views here.

def user_login(request):
    if request.method == 'GET':
        return render_to_response('account/login.html',{'title':'用户登录--工大CSDN俱乐部'},
                                  context_instance=RequestContext(request))
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        u = authenticate(username=username, password=password)
        if not User.objects.filter(username=username).exists():
            messages.add_message(request, messages.WARNING, 'username is not exist')
            return render_to_response('account/login.html', {'login': False},
                                      context_instance=RequestContext(request))
        elif not u:
            messages.add_message(request, messages.WARNING, 'password is invalid')
            return render_to_response('account/login.html',
                                      context_instance=RequestContext(request))
        login(request, u)
        return render_to_response('index.html', {'username': username,
                                                 'login': True,
                                                 'request': request},
                                  context_instance=RequestContext(request))


def user_signup(request):
    if request.method == 'GET':
        return render_to_response('account/signup.html',{'title':u'学生注册--工大CSDN俱乐部'},
                                  context_instance=RequestContext(request))
    elif request.method == 'POST':
        username = request.POST['username']
        number = request.POST['number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1)
            u = authenticate(username=username, password=password1)
        else:
            messages.add_message(request, messages.WARNING, _(''))
            return render_to_response('account/login.html',
                                      context_instance=RequestContext(request))
        login(request, u)
        p = profile()
        p.number = number
        p.username = username
        p.user = user
        p.save()
        return HttpResponseRedirect(reverse('index'))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def index(request):
    return render_to_response('index.html', {'user': request.user,'title':u'大连工业大学CSDN俱乐部--We run cool events'},
                              context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', )


def user_profile(request, user_id):
    p = User.objects.get(id=user_id)
    return render_to_response('account/user.html', {'p': p, 'title':u'个人信息--%s'%(p.username),
                                                    'user': request.user})


def teacher_signup(request):
    if request.method == 'GET':
        return render_to_response('account/teacher-signup.html',{'title':'教师注册--工大CSDN俱乐部'},
                                  context_instance=RequestContext(request))
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = '%s@dlpu.edu.cn' % (email)
        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1, email=email)
            u = authenticate(username=username, password=password1)
        else:
            messages.add_message(request, messages.WARNING, _(u'输入的密码不一致 !'))
            return render_to_response('account/teacher-signup.html',
                                      context_instance=RequestContext(request))
        login(request, u)
        p = profile()
        p.user = user
        p.username = username
        p.identity = 0
        p.temp = '%s %s %s'%(username,password1,email)
        p.save()
        url = base64.encodestring(p.temp)
        send_mail(u'教师身份验证', u'尊敬的老师，点击后面的链接验证您在工大CSDN的教师身份，以便您能正常的使用作业发布等功能。'
                             u'http://dlpucsdn.com/confirm/%s' % (url),
                  'admin@dlpucsdn.com', [email])
        messages.add_message(request,messages.WARNING,_(u'已经向您的邮箱%s发送了验证邮件，请注意查收！'%(email)))
    return render_to_response('index.html',
                              context_instance=RequestContext(request))

def confirm_identity(request,t):
    s = base64.decodestring(t)
    l = re.split('\s+',s)
    username = l[0]
    password = l[1]
    u = authenticate(username=username,password=password)
    login(request,u)
    u = profile.objects.get(username = username)
    u.identity = 2
    u.save()
    messages.add_message(request,messages.WARNING,_(u'您已认证成功，可以使用作业发布功能啦~'))
    return HttpResponseRedirect(reverse('index'))

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from account.models import profile
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
# Create your views here.

def user_login(request):
    if request.method == 'GET':
        return render_to_response('account/login.html',
                                  context_instance=RequestContext(request))
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        u = authenticate(username=username, password=password)
        if not User.objects.filter(username=username).exists():
            messages.add_message(request, messages.WARNING, 'username is not exist')
            return render_to_response('index.html', {'login': False},
                                      context_instance=RequestContext(request))
        elif not u:
            messages.add_message(request, messages.WARNING, 'password is invalid')
            return render_to_response('account/login.html',
                                      context_instance=RequestContext(request))
        login(request,u)
        return render_to_response('index.html', {'username': username,
                                                 'login': True,
                                                 'request':request},
                                  context_instance=RequestContext(request))


def user_signup(request):
    if request.method == 'GET':
        return render_to_response('account/signup.html',
                                  context_instance=RequestContext(request))
    elif request.method == 'POST':
        username = request.POST['username']
        number = request.POST['number']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1, email=email)
            u = authenticate(username=username, password=password1, email=email)
        else:
            return render_to_response('account/login.html',
                                      context_instance=RequestContext(request))
        login(request, u)
        p = profile()
        p.number = number
        p.user = user
        p.save()
        return render_to_response('index.html',{'username':username},
                                  context_instance=RequestContext(request))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def index(request):
    return render_to_response('index.html',{'user':request.user})

def about(request):
    return render_to_response('about.html')
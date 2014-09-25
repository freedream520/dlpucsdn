from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpRequest,HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from account.models import Profile
from django.template import RequestContext
# Create your views here.

def user_login(request):
    if request.method=='GET':
        return render_to_response('account/login.html',{'hello':'get method'},
                                  context_instance=RequestContext(request))
    elif request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        number = request.POST['number']
        user = User.objects.create_user(username=username,password=password)
        user = authenticate(username=username,password=password)
        login(request,user)
        p = Profile()
        p.number = number
        p.user = user
        p.save()
        login(request,user)
        return render_to_response('index.html',{'login':'login!!!'},
                                  context_instance=RequestContext(request))


def user_signup(request):
    if request.method == 'GET':
        return render_to_response('account/signup.html',{'hello':'hellooooo'})
    elif request.method =='POST':
        username = request.POST.get('username')
        number = request.POST.get('number')
        password = request.POST.get('password')
        user = Profile(username=username,number=number,password=password)
        user.save()
        return render_to_response('home/index.html',{'username':username,'number':number,'password':password})
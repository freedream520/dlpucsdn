from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpRequest,HttpResponseRedirect,HttpResponse
from django.contrib import auth
from account.models import Profile
# Create your views here.
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
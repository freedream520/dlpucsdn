from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.
def user_login(request):

    return render_to_response('account/login.html',{'zuoye':'active'})
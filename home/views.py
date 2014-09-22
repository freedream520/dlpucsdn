from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
def home(request):
    username = request.GET
    return render_to_response('home/index.html',{'title':'dlpucsdn'})

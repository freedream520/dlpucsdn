from django.shortcuts import render,render_to_response
from account.models import department,profile

# Create your views here.
def assignment_index(request):
    return render_to_response('assignment/index.html',{'user':request.user,
                                                       })

def assignment_issue(request):
    return  render_to_response('assignment/issue.html',{'user':request.user,
                                                        })


from django.shortcuts import render,render_to_response

# Create your views here.
def assignment_main(request):
    return render_to_response('assignment/index.html')

def assignment_issue(request):
    return  render_to_response('assignment/issue.html')
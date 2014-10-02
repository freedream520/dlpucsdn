from django.shortcuts import render,render_to_response

# Create your views here.
def topic_list(request):
    return render_to_response('forum/index.html')

def create_topic(request):
    return render_to_response('forum/create.html')
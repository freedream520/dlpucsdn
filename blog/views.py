from django.shortcuts import render,render_to_response

# Create your views here.
def blog_list(request):
    return render_to_response('blog/index.html')

def write_blog(request):
    return render_to_response('blog/write.html')
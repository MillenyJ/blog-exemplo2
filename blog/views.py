from django.shortcuts import render
from .models import Post,Blog

def index(request):
    context = {
        "posts": Post.objects.all() ,
        "blog": Blog.objects.first(),
    }
    return render(request, "index.html", context)

def post(request, post_id):
    context = {
        "post": Post.objects.get(pk=post_id),
        "blog": Blog.objects.first(),
    }
    return render(request, "post.html", context)
    
def about(request):
   
    context = {
        "blog": Blog.objects.first(),
    }
    return render(request, "about.html")

def contact(request): 
    context = {
        "blog": Blog.objects.first(),
    }
    if request.method == "POST":
        print (request.method)
        return render(request, "contact.html", context)
    else:
        return render(request, "contact.html", context)
    
    

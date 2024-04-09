from django.shortcuts import render
from .models import Post

def blog_view(request):
    posts = Post.objects.all()
    return render(request, "a_blog/blog_home.html", posts=posts)

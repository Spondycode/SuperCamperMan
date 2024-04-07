from django.shortcuts import render

def blog_view(request):
    return render(request, "a_blog/blog.html")

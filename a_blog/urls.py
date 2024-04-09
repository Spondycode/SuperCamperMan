from django.urls import path
from a_blog.views import blog_view

urlpatterns = [
    path('', blog_view, name="blog-home"),
]

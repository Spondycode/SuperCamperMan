from django.shortcuts import render
from .models import News

def news_view(request):
    posts = News.objects.all()
    return render(request, 'a_news/news.html', {'posts': posts})

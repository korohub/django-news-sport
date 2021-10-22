from django.shortcuts import render
from django.http import HttpResponse

import requests

# Create your views here.

def index(request): 
    res = requests.get("https://newsapi.org/v2/top-headlines?country=fr&category=sports&apiKey=3cf942b690324abda97765b93cc2bc3a")
    jsonRes = res.json()
    articles = jsonRes['articles']
    return render(request, 'blog/index.html', {'articles': articles} )


def specific(request):
    list1 = [1,2,3,4]
    return HttpResponse(list1)

def article(request, article_id ):    
    return render(request, 'blog/index.html', {'article_id': article_id})

def singleArticle(request):    
    title = request.POST.get('title')
    content = request.POST.get('content')
    img = request.POST.get('img')

    return render(request, 'blog/single_article.html', {'title': title, 'content': content, 'img': img})

def contact(request):
    return render(request, 'blog/contact.html')

def about(request):
    return render(request, 'blog/about.html')

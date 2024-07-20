from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import *

# Create your views here.

class ArticleListView(ListView):
    def get(self , request):
        articles = ArticleModel.objects.filter(is_active=True)
        return render(request , 'article-list.html' , context={
            'articles':articles,
        })

class ArticleDetailView(View):
    def get(self , request , slug):
        article = ArticleModel.objects.filter(slug=slug).first()
        tags = ArticleTagModel.objects.filter(articlemodel=article)
        return render(request , 'article-detail.html' , context={
            'article':article,
            'tags':tags,
        })

class ArticleTagsView(View):
    def get(self , request , tag_slug):
        articles = ArticleModel.objects.filter(tag__slug=tag_slug)
        return render(request , 'article-list.html' , context={
            'articles':articles,
        })


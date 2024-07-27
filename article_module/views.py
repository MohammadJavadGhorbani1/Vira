from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import *
from django.http import HttpResponse , Http404
from django.template.loader import render_to_string

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
        comments = ArticleCommentModel.objects.filter(article__slug=slug , is_publish=True , parent_comment=None)
        tags = ArticleTagModel.objects.filter(articlemodel=article)
        return render(request , 'article-detail.html' , context={
            'article':article,
            'tags':tags,
            'comments':comments,
        })

def comment_sending(request):
    article_id = request.GET.get('article_id')
    comment_parent = request.GET.get('parent')
    article = ArticleModel.objects.filter(id=article_id).first()
    if article is not None:
        if comment_parent:
            user_id = request.user.id
            text = request.GET.get('text')
            new_comment = ArticleCommentModel(article_id=article_id , user_id=user_id , text=text , parent_comment_id=comment_parent)
            new_comment.save()
            # success = True
            return HttpResponse('asjfkbmmkg')
        else:
            user_id = request.user.id
            text = request.GET.get('text')
            new_comment = ArticleCommentModel(article_id=article_id, user_id=user_id, text=text , parent_comment_id=None)
            new_comment.save()
            return HttpResponse('sfdcfgcgcgdfgfdfd')
    else:
        raise HttpResponse('error')

def comments_like(request):
    comment_id = request.GET.get('comment_id')
    comment = ArticleCommentModel.objects.filter(id=comment_id).first()
    if comment is not None:
        like = request.GET.get('like')
        if like == 'true':
            comment.comment_like += 1
            comment.save()
            return HttpResponse('thanks')
        else:
            comment.comment_dislike += 1
            comment.save()
            return HttpResponse('thanks')
    else:
        return HttpResponse('error')
class ArticleTagsView(View):
    def get(self , request , tag_slug):
        articles = ArticleModel.objects.filter(tag__slug=tag_slug)
        return render(request , 'article-list.html' , context={
            'articles':articles,
        })


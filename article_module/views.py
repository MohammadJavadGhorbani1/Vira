from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import *
from django.http import HttpResponse, Http404, JsonResponse
from django.template.loader import render_to_string


# Create your views here.

class ArticleListView(ListView):
    def get(self, request):
        user = request.user
        articles = ArticleModel.objects.filter(is_active=True)
        new_articles = ArticleModel.objects.filter(is_active=True).order_by('-id')[:5]
        comments = ArticleCommentModel.objects.filter(is_publish=True, user=user).order_by('-id')[:5]
        return render(request, 'article-list.html', context={
            'articles': articles,
            'new_articles': new_articles,
            'comments': comments,
        })


class ArticleDetailView(View):
    def get(self, request, slug):
        user = request.user
        article = ArticleModel.objects.filter(slug=slug).first()
        comments = ArticleCommentModel.objects.filter(article__slug=slug, is_publish=True, parent_comment=None)
        tags = ArticleTagModel.objects.filter(articlemodel=article)
        new_articles = ArticleModel.objects.filter(is_active=True).order_by('-id')[:5]
        new_comments = ArticleCommentModel.objects.filter(is_publish=True, user=user).order_by('-id')[:5]
        return render(request, 'article-detail.html', context={
            'article': article,
            'tags': tags,
            'comments': comments,
            'new_articles': new_articles,
            'new_comments': new_comments,
        })


def comment_sending(request):
    article_id = request.GET.get('article_id')
    comment_parent = request.GET.get('parent')
    article = ArticleModel.objects.filter(id=article_id).first()
    if article is not None:
        if comment_parent:
            user_id = request.user.id
            text = request.GET.get('text')
            new_comment = ArticleCommentModel(article_id=article_id, user_id=user_id, text=text,
                                              parent_comment_id=comment_parent)
            new_comment.save()
            # success = True
            return JsonResponse({'status': 'anwser-success'})
        else:
            user_id = request.user.id
            text = request.GET.get('text')
            new_comment = ArticleCommentModel(article_id=article_id, user_id=user_id, text=text, parent_comment_id=None)
            new_comment.save()
            return JsonResponse({'status': 'success'})
    else:
        raise JsonResponse({'status': 'id-error'})


def comments_like(request):
    like_dict = {}
    dislike_dict = {}
    comment_id = request.GET.get('comment_id')
    comment = ArticleCommentModel.objects.filter(id=comment_id).first()
    if comment is not None:
        user_id = str(request.user.id)
        like = request.GET.get('like')
        if like == 'true':
            if user_id in dislike_dict.keys():
                print(1)
                print(dislike_dict)
                dislike_dict.pop(user_id)
                comment.comment_like += 1
                comment.comment_dislike -= 1
                comment.save()
                return HttpResponse('thanks')
            else:
                if user_id in like_dict.keys():
                    like_dict.pop(user_id)
                    print(like_dict)
                    comment.comment_like -= 1
                    comment.save()
                    return HttpResponse('thanks')
                else:
                    like_dict.update({user_id : comment_id})
                    print(like_dict)
                    comment.comment_like += 1
                    comment.save()
                    # print(like_list)
                    return HttpResponse('thanks')
        else:
            if user_id in like_dict:
                like_dict.pop(user_id)
                comment.comment_dislike += 1
                comment.comment_like -= 1
                comment.save()
                return HttpResponse('thanks')
            else:
                if user_id in dislike_dict:
                    dislike_dict.pop(user_id)
                    comment.comment_dislike -= 1
                    comment.save()
                    return HttpResponse('thanks')
                else:
                    dislike_dict.update({user_id : comment_id})
                    print(dislike_dict)
                    comment.comment_dislike += 1
                    comment.save()
                    return HttpResponse('thanks')
    else:
        return HttpResponse('error')


class ArticleTagsView(View):
    def get(self, request, tag_slug):
        articles = ArticleModel.objects.filter(tag__slug=tag_slug)
        return render(request, 'article-list.html', context={
            'articles': articles,
        })

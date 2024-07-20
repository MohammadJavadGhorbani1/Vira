from django.urls import path
from .views import *

urlpatterns = [
    path('' , ArticleListView.as_view() , name='article-list-page'),
    path('details/<slug>' , ArticleDetailView.as_view() , name='article-detail-page'),
    path('tags/<tag_slug>' , ArticleTagsView.as_view() , name='article-tags-page'),
]

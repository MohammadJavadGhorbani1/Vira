from django.urls import path
from .views import *

urlpatterns = [
    path('' , MainDashbord.as_view() , name='main-dashbord-page'),
    path('edit-dashbord/' , EditDashbordView.as_view() , name='edit-dashbord-page'),
    path('dash-password-edit/' , EditPasswordDashView.as_view() , name='edit-password-dash-page'),
    path('user-wishlist/' , DashbordWishListView.as_view() , name='dashbord-wishlist-page'),
    path('notifs/' , DashbordNotifsView.as_view() , name='dashbord-notifs-page'),
    path('delete-wishlist-product/' , wishlistdelete),
    path('news/' , DashbordNewsView.as_view() , name='dashbord-news-page'),
    path('user-comments/' , DashbordCommentsView.as_view() , name='dashbord-comments-page'),
]

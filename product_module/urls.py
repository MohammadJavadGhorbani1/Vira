from django.urls import path
from .views import *

urlpatterns = [
    path('' , ProductList.as_view() , name= 'product_list'),
    path('details/<slug>' , ProductDetails.as_view() , name= 'product_details'),
    path('categories/<category_slug>' , CategoryDetails.as_view() , name= 'category_detail'),
    path('parent-categories/<parent_category_slug>' , ParentCategoryDetails.as_view() , name='parent-category-detail'),
    path('tags/<tag_slug>' , ProductTag.as_view() , name='product_tag'),
    path('new-products/' , ProductByID.as_view() , name='new-products-page'),
    path('add-to-wishlist/' , addwishlistproduct),
    path('details/no-product/<slug>' , ProductDetails.as_view() , name='no-product-page'),
    path('add-notif/' , addproductnotif),
    path('send-comment/' , productcomments),
    # path('change-category/' , product_categories),
]
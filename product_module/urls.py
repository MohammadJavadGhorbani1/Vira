from django.urls import path
from .views import *

urlpatterns = [
    path('' , ProductList.as_view() , name= 'product_list'),
    path('details/<slug>' , ProductDetails.as_view() , name= 'product_details'),
    path('categories/<category_slug>' , CategoryDetails.as_view() , name= 'category_detail'),
    path('parent-categories/<parent_category_slug>' , ParentCategoryDetails.as_view() , name='parent-category-detail'),
    path('tags/<tag_slug>' , ProductTag.as_view() , name='product_tag'),
]
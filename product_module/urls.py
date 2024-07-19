from django.urls import path
from .views import *

urlpatterns = [
    path('' , ProductList.as_view() , name= 'product_list'),
    path('details/<slug>' , ProductDetails.as_view() , name= 'product_details'),
    # path('products/categories/' , ProductCategories.as_view() , name= 'product_category'),
    path('categories/<category_slug>' , CategoryDetails.as_view() , name= 'category_detail'),
    # path('tags/<tag_slug>' , ProductTags.as_view() , name='product_tag'),
]
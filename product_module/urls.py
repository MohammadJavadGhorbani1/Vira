from django.urls import path
from .views import *

urlpatterns = [
    path('products/' , ProductList.as_view() , name= 'product_list'),
    path('products/details/<slug>' , ProductDetails.as_view() , name= 'product_details'),
    path('products/categories/' , ProductCategories.as_view() , name= 'product_category'),
    path('products/categories/details/<url_title>' , CategoryDetails.as_view() , name= 'category_detail'),
    # path('products/tags/<url_tag>' , Product_Tags , name='product_tag'),
]
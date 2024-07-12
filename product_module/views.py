from django.shortcuts import render
from .models import *
from django.views import View
from django.views.generic import ListView,DetailView

# Create your views here.

class ProductList(ListView):
    template_name = 'products_list.html'
    model = Products
    context_object_name = 'products'
    def get_queryset(self):
        query = super(ProductList , self).get_queryset()
        context = query.filter(is_active=True)
        return context

# class ProductDetails(DetailView):
#     template_name = 'product_detail.html'
#     model = Products
#     context_object_name = 'product'
#     def get_queryset(self):
#         query = super(ProductDetails , self).get_queryset()
#         context = query.filter(products=product)
#         return context


# class ProductList(View):
#     def get(self , request):
#         products = Products.objects.filter(is_active=True)
#         return render(request, 'products_list.html', {
#             'products': products
#         })

class ProductDetails(View):
    def get(self , request , slug):
        product = Products.objects.get(slug=slug)
        tags = ProductTags.objects.filter(products=product)
        return render(request, 'product_detail.html', {
        'product': product ,
        'tags': tags
        })

class ProductCategories(View):
    def get(self , request):
        categories = ParentProductCategory.objects.all()
        child_categories = ChildProductCategory.objects.all()
        return render(request, 'category_list.html', {
            'categories': categories,
            'child_categories': child_categories
        })

class CategoryDetails(View):
    def get(self , request , url_title):
        child_categories = ChildProductCategory.objects.filter(url_title=url_title)
        product = Products.objects.all()
        return render(request, 'category_detail.html', {
            'child_categories': child_categories,
            'product':product
        })

# def Product_List(request):
#     products = Products.objects.filter(is_active=True)
#     return render(request , 'products_list.html' , {
#     'products':products
#     })

# def Product_Category(request):
#     categories = ParentProductCategory.objects.all()
#     child_categories = ChildProductCategory.objects.all()
#     return render(request , 'category_list.html' , {
#         'categories':categories,
#         'child_categories':child_categories
#     })

# def Product_Detail(request , slug):
#     product = Products.objects.get(slug=slug)
#     tags = ProductTags.objects.filter(products=product)
#     return render(request, 'product_detail.html', {
#     'product': product ,
#     'tags': tags
#     })

# def Category_Detail(request , categorys_id):
#     products = Products.objects.filter(category__id=categorys_id)
#     return render(request , 'category_detail.html' , {
#         'products':products
#     })

# def Product_Tags(request , url_tag):
#      tags = ProductTags.objects.filter(url_title=url_tag)
#      return render(request , 'products_tags.html' , {
#         'tags':tags
#      })

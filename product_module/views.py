from django.shortcuts import render
from .models import *
from django.views import View
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse, JsonResponse
from userpanel_module.models import *
from django.template.loader import render_to_string


# Create your views here.

# class ProductList(ListView):
#     template_name = 'products_list.html'
#     model = Products
#     context_object_name = 'products'
#     paginate_by = 2
#     def get_queryset(self):
#         query = super(ProductList , self).get_queryset()
#         context = query.filter(is_active=True)
#         return context

# class ProductDetails(DetailView):
#     template_name = 'product_detail.html'
#     model = Products
#     context_object_name = 'product'
#     def get_queryset(self):
#         query = super(ProductDetails , self).get_queryset()
#         context = query.filter(products=product)
#         return context


class ProductList(View):
    def get(self, request):
        products = Products.objects.filter(is_active=True).order_by('-visit')
        new_products = Products.objects.filter(is_active=True).order_by('-id')
        paginator = Paginator(products, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'products_list.html', {
            # 'products': products
            'page_obj': page_obj,
            'paginator': paginator,
            'new_products':new_products,
        })


class ProductDetails(View):
    def get(self, request, slug):
        product:Products = Products.objects.filter(slug=slug).first()
        tags = ProductTags.objects.filter(products=product)
        comments = ProductCommentsModel.objects.filter(product_id=product.id , is_publish=True , parent_comment=None)
        if product.count < 1:
            product.is_active = False
            product.visit += 1
            product.save()
            likely_products = Products.objects.filter(category__parent_category_id=product.category.parent_category.id,is_active=True)
            return render(request, 'no-product.html', {
                'product': product,
                'tags': tags,
                'likely_products': likely_products,
                'comments':comments,
            })
        if product.is_active:
            product.visit += 1
            product.save()
            return render(request, 'product_detail.html', {
                'product': product,
                'tags': tags,
                'comments':comments,
            })
        else:
            product.visit += 1
            product.save()
            likely_products = Products.objects.filter(category__parent_category_id=product.category.parent_category.id,is_active=True)
            return render(request, 'no-product.html', {
                'product': product,
                'tags': tags,
                'likely_products': likely_products,
                'comments':comments,
            })


# class ProductCategories(View):
#     def get(self , request):
#         categories = ParentProductCategory.objects.all()
#         child_categories = ChildProductCategory.objects.all()
#         return render(request, 'category_list.html', {
#             'categories': categories,
#             'child_categories': child_categories
#         })

class CategoryDetails(View):
    def get(self, request, category_slug):
        products = Products.objects.filter(category__slug=category_slug)
        paginator = Paginator(products, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'products_list.html', {
            # 'products': products
            'page_obj': page_obj,
            'paginator': paginator,
        })


class ParentCategoryDetails(View):
    def get(self, request, parent_category_slug):
        products = Products.objects.filter(category__parent_category__slug=parent_category_slug)
        paginator = Paginator(products, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'products_list.html', {
            # 'products': products
            'page_obj': page_obj,
            'paginator': paginator,
        })


class ProductTag(View):
    def get(self, request, tag_slug):
        products = Products.objects.filter(tags__slug=tag_slug)
        paginator = Paginator(products, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'products_list.html', {
            # 'products': products
            'page_obj': page_obj,
            'paginator': paginator,
        })


class ProductByID(View):
    def get(self, request):
        products = Products.objects.filter(is_active=True).order_by('-id')
        paginator = Paginator(products, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'products_list.html', {
            # 'products': products
            'page_obj': page_obj,
            'paginator': paginator,
        })


def addwishlistproduct(request):
    user = request.user
    if user.is_authenticated:
        product_id = request.GET.get('product_id')
        if product_id is not None:
            new_wishlist, create = WishlistProducts.objects.get_or_create(product_id=product_id, user=user)
            if create:
                return JsonResponse({'status': 'success'})
            else:
                if new_wishlist.is_active == True:
                    new_wishlist.is_active = False
                    new_wishlist.save()
                    return JsonResponse({'status': 'deleted'})
                else:
                    new_wishlist.is_active = True
                    new_wishlist.save()
                    return JsonResponse({'status': 'success'})
            new_wishlist.save()
            return HttpResponse('good')
        else:
            return JsonResponse({'status': 'id-error'})
    else:
        raise Http404


def addproductnotif(request):
    user = request.user
    if user.is_authenticated:
        product_id = request.GET.get('product_id')
        if product_id is not None:
            new_notif, create = ProductNotifModel.objects.get_or_create(user=user, product_id=product_id)
            if create:
                return JsonResponse({'status': 'success'})
            else:
                if new_notif.is_active == True:
                    new_notif.is_active = False
                    new_notif.save()
                    return JsonResponse({'status': 'deleted'})
                else:
                    new_notif.is_active = True
                    new_notif.save()
                    return JsonResponse({'status':'success'})
        else:
            return JsonResponse({'status': 'id-error'})
    else:
        raise Http404

def productcomments(request):
    user = request.user
    product_id = request.GET.get('product_id')
    product = Products.objects.filter(id=product_id).first()
    if product is not None:
        text = request.GET.get('text')
        parent = request.GET.get('parent')
        if parent:
            new_comment = ProductCommentsModel(product_id=product_id , user_id=user.id , text=text , parent_comment_id=parent)
            new_comment.save()
            return JsonResponse({'status':'anwser-success'})
        else:
            new_comment = ProductCommentsModel(product_id=product_id , user_id=user.id , text=text , parent_comment=None)
            new_comment.save()
            return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'id-error'})

# def product_categories(request):
#     most_visited = request.GET.get('most_visited')
#     if most_visited:
#         products = Products.objects.filter(is_active=True).order_by('-visit')
#         paginator = Paginator(products, 2)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         data = {
#             'page_obj':page_obj,
#             'paginator':paginator
#         }
#         return JsonResponse({
#             'status':'success',
#             'body':render_to_string('product-carts.html' , data)
#         })
#     else:
#         most_sells = request.GET.get('most_sells')
#         if most_sells:
#             products = Products.objects.filter(is_active=True).order_by('-count')
#             paginator = Paginator(products, 2)
#             page_number = request.GET.get('page')
#             page_obj = paginator.get_page(page_number)
#             data = {
#                 'page_obj':page_obj,
#                 'paginator':paginator
#             }
#             return JsonResponse({
#                 'status':'success',
#                 'body':render_to_string('product-carts.html' , data)
#             })
#         else:
#             most_new = request.GET.get('most_new')
#             if most_new:
#                 products = Products.objects.filter(is_active=True).order_by('-id')
#                 paginator = Paginator(products, 2)
#                 page_number = request.GET.get('page')
#                 page_obj = paginator.get_page(page_number)
#                 data = {
#                     'page_obj':page_obj,
#                     'paginator':paginator
#                 }
#                 return JsonResponse({
#                     'status':'success',
#                     'body':render_to_string('product-carts.html' , data)
#                 })
#             else:
#                 most_cheap = request.GET.get('most_cheap')
#                 if most_cheap:
#                     products = Products.objects.filter(is_active=True).order_by('price')
#                     paginator = Paginator(products, 2)
#                     page_number = request.GET.get('page')
#                     page_obj = paginator.get_page(page_number)
#                     data = {
#                         'page_obj':page_obj,
#                         'paginator':paginator
#                     }
#                     return JsonResponse({
#                         'status':'success',
#                         'body':render_to_string('product-carts.html' , data)
#                     })
#                 else:
#                     most_expensive = request.GET.get('most_expensive')
#                     products = Products.objects.filter(is_active=True).order_by('-id')
#                     paginator = Paginator(products, 2)
#                     page_number = request.GET.get('page')
#                     page_obj = paginator.get_page(page_number)
#                     data = {
#                         'page_obj':page_obj,
#                         'paginator':paginator
#                     }
#                     return JsonResponse({
#                         'status':'success',
#                         'body':render_to_string('product-carts.html' , data)
#                     })

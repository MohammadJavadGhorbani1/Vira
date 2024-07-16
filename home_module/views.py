from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from product_module.models import *

# Create your views here.

# class HomePage(View):
#     def get(self , request):
#         return render(request , 'home.html' , {
#
#         })

class HomePage(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super(HomePage , self).get_context_data(**kwargs)
        return context

def header_render_partial(request):
    categories = ProductCategory.objects.filter(parent_category=None)
    # child_categories = ProductCategory.objects.filter(parent_category=not None)
    return render(request , 'header.html' , {
        'categories':categories,
        # 'child_categories':child_categories,
    })

# class CategoryDetails(View):
#     def get(self , request , id):
#         products = Products.objects.filter(category_id=id)
#         return render(request, 'products_list.html', {
#             'products': products,
#         })

def footer_render_partial(request):
    return render(request , 'footer.html' , {

    })

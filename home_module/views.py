from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from product_module.models import *
from sitesettings_module.models import *
from article_module.models import *

# Create your views here.

class HomePage(View):
    def get(self , request):
        sliders = SliderSettingsModel.objects.filter(is_active=True)
        ads = AdsSettingsModel.objects.filter(is_active=True).first()
        articles = ArticleModel.objects.filter(is_active=True)
        categories = ProductCategory.objects.filter(parent_category=None)
        return render(request , 'home.html' , {
            'sliders':sliders,
            'ads':ads,
            'articles':articles,
            'categories':categories,
        })

# class HomePage(TemplateView):
#     template_name = 'home.html'
#     def get_context_data(self, **kwargs):
#         context = super(HomePage , self).get_context_data(**kwargs)
#         return context

def header_render_partial(request):
    settings = SiteSettingsModel.objects.filter(is_active=True).first()
    categories = ProductCategory.objects.filter(parent_category=None)
    # child_categories = ProductCategory.objects.filter(parent_category=not None)
    return render(request , 'header.html' , {
        'categories':categories,
        'settings':settings,
        # 'child_categories':child_categories,
    })

# class CategoryDetails(View):
#     def get(self , request , id):
#         products = Products.objects.filter(category_id=id)
#         return render(request, 'products_list.html', {
#             'products': products,
#         })

def footer_render_partial(request):
    settings = SiteSettingsModel.objects.filter(is_active=True).first()
    return render(request , 'footer.html' , {
        'settings':settings,
    })

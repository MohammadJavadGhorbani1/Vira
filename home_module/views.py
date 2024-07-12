from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

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
    return render(request , 'header.html' , {

    })

def footer_render_partial(request):
    return render(request , 'footer.html' , {

    })

from django.shortcuts import render
from django.views import View
from user_module.models import User
from django.http import Http404


# Create your views here.

class MainDashbord(View):
    def get(self , request):
        return render(request , 'main-dashbord.html' , context={

        })

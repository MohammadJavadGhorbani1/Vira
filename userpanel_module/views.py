from django.shortcuts import render , redirect
from django.views import View
from user_module.models import User
from django.http import Http404 , HttpResponse , JsonResponse
from .forms import *
from django.contrib.auth import logout
from .models import *
from sitesettings_module.models import *
from article_module.models import *


# Create your views here.

class MainDashbord(View):
    def get(self , request):
        user = request.user
        wishlist_products = WishlistProducts.objects.filter(is_active=True , user=user)[:3]
        return render(request , 'dashbord-info.html' , context={
            'wishlist_products':wishlist_products,
        })

class EditDashbordView(View):
    def get(self , request):
        user = request.user
        if user.is_authenticated:
            edit_form = EditDashbordForm(instance=user)
            return render(request , 'dashbord-edit.html' , context={
                'edit_form':edit_form,
                'error':False
            })
        else:
            raise Http404
    def post(self , request):
        user = request.user
        edit_form = EditDashbordForm(request.POST , request.FILES , instance=user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
            return render(request, 'dashbord-edit.html', context={
                'edit_form': edit_form,
                'error': False,
                'success':True
            })
        else:
            edit_form.add_error('first_name' , 'لطفا تمامی مشخصات را وارد کنید')
            return render(request, 'dashbord-edit.html', context={
                'edit_form': edit_form,
                'error': True
            })

class EditPasswordDashView(View):
    def get(self , request):
        user = request.user
        password_form = EditPasswordDashForm()
        if user.is_authenticated:
            return render(request , 'dash-password-change.html' , context={
                'password_form':password_form,
            })
        else:
            raise Http404
    def post(self , request):
        user = request.user
        password_form = EditPasswordDashForm(request.POST)
        if password_form.is_valid():
            old_password = password_form.cleaned_data.get('old_password')
            if user.check_password(old_password):
                new_password = password_form.cleaned_data.get('new_password')
                re_password = password_form.cleaned_data.get('re_password')
                if len(new_password) > 7:
                    if new_password == re_password:
                        user.set_password(new_password)
                        user.save()
                        logout(request)
                        return redirect('login_page')
                    else:
                        password_form.add_error('old_password' , 'لطفا تکرار رمز عبور را صحیح وارد کنید')
                        return render(request , 'dash-password-change.html' , context={
                            'password_form':password_form,
                            'error':True,
                        })
                else:
                    password_form.add_error('old_password', 'رمز عبور شما باید حداقل شامل هشت کاراکتر باشد')
                    return render(request, 'dash-password-change.html', context={
                        'password_form': password_form,
                        'error': True,
                    })
            else:
                password_form.add_error('old_password', 'رمز عبور قبلی شما اشتباه است')
                return render(request, 'dash-password-change.html', context={
                    'password_form': password_form,
                    'error': True,
                })
        else:
            password_form.add_error('old_password', 'لطفا تمامی مشخصات را وارد کنید')
            return render(request, 'dash-password-change.html', context={
                'password_form': password_form,
                'error': True,
            })

class DashbordWishListView(View):
    def get(self , request):
        user = request.user
        wishlist_products = WishlistProducts.objects.filter(user=user , is_active=True)
        return render(request , 'dashbord-wishlist.html' , context={
            'wishlist_products':wishlist_products,
        })

class DashbordNotifsView(View):
    def get(self , request):
        notifs = NotifModel.objects.filter(is_active=True)
        return render(request , 'dashbord-notifs.html' , context={
            'notifs':notifs,
        })

class DashbordNewsView(View):
    def get(self , request):
        user = request.user
        notif_products = ProductNotifModel.objects.filter(user=user , product__is_active=True , is_active=True)
        return render(request , 'dashbord-news.html' , context={
            'notif_products':notif_products,
        })

class DashbordCommentsView(View):
    def get(self , request):
        user = request.user
        article_comments = ArticleCommentModel.objects.filter(user=user , parent_comment=None)
        product_comments = ProductCommentsModel.objects.filter(user=user , parent_comment=None)
        return render(request , 'dashbord-comments.html' , context={
            'article_comments':article_comments,
            'product_comments':product_comments,
        })





def basedashbord(request):
    return render(request , 'main-dashbord.html' , context={

    })

def wishlistdelete(request):
    user = request.user
    product_id = request.GET.get('product_id')
    if product_id is not None:
        wishlist:WishlistProducts = WishlistProducts.objects.filter(user=user , product_id=product_id).first()
        wishlist.is_active = False
        wishlist.save()
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'id-error'})

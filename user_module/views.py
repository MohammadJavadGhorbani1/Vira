from django.shortcuts import render
from django.views import View
from .forms import *
from .models import *
from django.utils.crypto import get_random_string
from django.shortcuts import redirect
from django.urls import reverse
from .utils import Random_Code, sms_sender
from django.http import Http404
from django.contrib.auth import login, logout
import re


# Create your views here.

class RegisterView(View):
    def get(self, request):
        register = RegisterForm
        global captcha
        captcha = get_random_string(6)
        return render(request, 'register.html', {
            'register': register,
            'captcha': captcha,
            'errors': False,
        })

    def post(self, request):
        register = RegisterForm(request.POST)
        if register.is_valid():
            firstname = register.cleaned_data.get('firstname')
            lastname = register.cleaned_data.get('lastname')
            username = register.cleaned_data.get('username')
            phone_number = register.cleaned_data.get('phone_number')
            password = register.cleaned_data.get('password')
            re_password = register.cleaned_data.get('re_password')
            capcha = request.POST.get('capcha')
            if re.fullmatch(r'^09(1[0-9]|2[0-9]|3[0-9]|9[0-9]|0[0-9])-?[0-9]{3}-?[0-9]{4}$' , phone_number):
                if capcha == captcha:
                    if len(password) > 7:
                        if password == re_password:
                            user = User.objects.filter(phone_number=phone_number).first()
                            if user is not None:
                                register.add_error('firstname', 'شما قبلا ثبت نام کرده اید لطفا وارد شوید')
                                return render(request, 'register.html', {
                                    'register': register,
                                    'captcha':captcha,
                                    'errors':True
                                })
                            else:
                                new_user = User(first_name=firstname, last_name=lastname, username=username , phone_number=phone_number , is_active=False , active_mobile=Random_Code.random_code() , token=get_random_string(70))
                                new_user.set_password(password)
                                new_user.save()
                                # sms_sender.send_sms(new_user.phone_number , new_user.active_mobile)
                                return redirect(reverse('confiremcode-page', args=[new_user.token]))
                        else:
                            register.add_error('firstname', 'لطفا در تکرار رمز عبور دقت کنید')
                            return render(request, 'register.html', {
                                'register': register,
                                'captcha': captcha,
                                'errors':True
                            })
                    else:
                        register.add_error('firstname', 'رمز عبور شما باید حداقل شامل 8 کاراکتر باشد')
                        return render(request, 'register.html', {
                            'register': register,
                            'captcha': captcha,
                            'errors':True
                        })
                else:
                    register.add_error('firstname', 'لطفا در وارد کردن کاراکترهای تصویر دقت کنید')
                    return render(request, 'register.html', {
                        'register': register,
                        'captcha': captcha,
                        'errors':True
                    })
            else:
                register.add_error('firstname', 'لطفا یک شماره تلفن معتبر وارد کنید')
                return render(request, 'register.html', {
                    'register': register,
                    'captcha': captcha,
                    'errors':True
                })
        else:
            register.add_error('firstname', 'لطفا تمامی مشخصات را وارد کنید')
            return render(request, 'register.html', {
                'register': register,
                'captcha': captcha,
                'errors':True
            })


class RegisterConfirmView(View):
    error_dict = {}
    def get(self, request, token):
        user = User.objects.filter(token=token).first()
        if user is not None:
            register_confirm = RegisterConfirmForm()
            return render(request, 'register-confirm.html', {
                'errors':False,
                'register_confirm': register_confirm
            })

    def post(self, request, token):
        user = User.objects.filter(token=token).first()
        if user is not None and user.is_active == False:
            register_confirm = RegisterConfirmForm(request.POST)
            if register_confirm.is_valid():
                code_active = register_confirm.cleaned_data.get('active_code')
                if code_active == user.active_mobile:
                    user.is_active = True
                    user.active_mobile = Random_Code.random_code()
                    user.token = get_random_string(70)
                    user.save()
                    try:
                        RegisterConfirmView.error_dict.pop(user.phone_number)
                    except:
                        pass
                    return redirect('home_page')
                else:
                    if user.phone_number in RegisterConfirmView.error_dict.keys():
                        error_num = RegisterConfirmView.error_dict[user.phone_number] + 1
                        register_confirm.add_error('active_code', f'کد وارد شده اشتباه است شما میتوانید {9 - int(RegisterConfirmView.error_dict[user.phone_number])} بار دیگر تلاش کنید')
                        if error_num > 9:
                            user.delete()
                            return redirect('register_page')
                        RegisterConfirmView.error_dict.update({user.phone_number: error_num})
                    else:
                        RegisterConfirmView.error_dict.update({user.phone_number : 1})
                        register_confirm.add_error('active_code', f'کد وارد شده اشتباه است شما میتوانید {10 - int(RegisterConfirmView.error_dict[user.phone_number])} بار دیگر تلاش کنید')
                    # register_confirm.add_error('active_code', 'کد وارد شده اشتباه است')
                    return render(request, 'register-confirm.html', {
                        'errors':True,
                        'register_confirm': register_confirm
                    })
            else:
                register_confirm.add_error('active_code', 'کد فعالسازی را وارد کنید')
                return render(request, 'register-confirm.html', {
                    'errors':True,
                    'register_confirm': register_confirm
                })
        else:
            # user.active_mobile = Random_Code.random_code()
            # user.token = get_random_string(70)
            # user.save()
            raise Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login.html', {
            'login_form': login_form,
            'errors': False
        })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            phone_number = login_form.cleaned_data.get('phone_number')
            password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(phone_number=phone_number).first()
            if user is not None:
                password_check = user.check_password(password)
                if password_check == True:
                    user.active_mobile = Random_Code.random_code()
                    user.token = get_random_string(70)
                    user.save()
                    login(request, user)
                    return redirect('home_page')
                else:
                    login_form.add_error('phone_number', 'شماره تلفن یا رمز عبور اشتباه است')
                    return render(request, 'login.html', {
                        'login_form': login_form,
                        'errors': True
                    })
            else:
                login_form.add_error('phone_number', 'شماره تلفن یا رمز عبور اشتباه است')
                return render(request, 'login.html', {
                    'login_form': login_form,
                    'errors': True
                })
        else:
            login_form.add_error('phone_number', 'شماره تلفن یا رمز عبور اشتباه است')
            return render(request, 'login.html', {
                'login_form': login_form,
                'errors': True
            })


class ForgetPasswordView(View):
    def get(self, request):
        forget = ForgetPasswordForm()
        return render(request, 'forget-password.html', context={
            'forget': forget,
            'errors': False
        })

    def post(self, request):
        forget = ForgetPasswordForm(request.POST)
        if forget.is_valid():
            phone_number = forget.cleaned_data.get('phone_number')
            user: User = User.objects.filter(phone_number=phone_number).first()
            if user is not None:
                return redirect(reverse('forget-confirm-page', args=[user.token]))
            else:
                forget.add_error('phone_number', 'لطفا یک شماره تماس صحیح وارد کنید')
                return render(request, 'forget-password.html', context={
                    'forget': forget,
                    'errors': True
                })
        else:
            forget.add_error('phone_number', 'لطفا یک شماره تلفن وارد کنید')
            return render(request, 'forget-password.html', context={
                'forget': forget,
                'errors': True
            })


class ForgetConfirmView(View):
    error_dict = {}
    def get(self, request, token):
        user = User.objects.filter(token=token).first()
        if user is not None:
            forget_confirm = ForgetConfirmForm()
            return render(request, 'forget-confirm.html', {
                'errors':False,
                'forget_confirm': forget_confirm
            })
        else:
            return redirect('register_page')

    def post(self, request, token):
        user = User.objects.filter(token=token).first()
        forget_confirm = ForgetConfirmForm(request.POST)
        if user is not None:
            if forget_confirm.is_valid():
                code_active = forget_confirm.cleaned_data.get('active_code')
                if code_active == user.active_mobile:
                    user.active_mobile = Random_Code.random_code()
                    user.token = get_random_string(70)
                    user.save()
                    try:
                        ForgetConfirmView.error_dict.pop(user.phone_number)
                    except:
                        pass
                    return redirect(reverse('change-password-page', args=[user.token , user.active_mobile]))
                else:
                    if user.phone_number in ForgetConfirmView.error_dict.keys():
                        error_num = ForgetConfirmView.error_dict[user.phone_number] + 1
                        forget_confirm.add_error('active_code', f'کد وارد شده اشتباه است شما میتوانید {3 - int(ForgetConfirmView.error_dict[user.phone_number])} بار دیگر تلاش کنید')
                        if error_num > 3:
                            user.active_mobile = Random_Code.random_code()
                            user.token = get_random_string(70)
                            user.save()
                            ForgetConfirmView.error_dict.pop(user.phone_number)
                            raise Http404
                        ForgetConfirmView.error_dict.update({user.phone_number : error_num})
                    else:
                        ForgetConfirmView.error_dict.update({user.phone_number : 1})
                        forget_confirm.add_error('active_code', f'کد وارد شده اشتباه است شما میتوانید {4 - int(ForgetConfirmView.error_dict[user.phone_number])} بار دیگر تلاش کنید')
                    return render(request, 'forget-confirm.html', {
                        'errors':True,
                        'forget_confirm': forget_confirm
                    })
            else:
                forget_confirm.add_error('active_code', 'کد فعالسازی را وارد کنید')
                return render(request, 'forget-confirm.html', {
                    'errors':True,
                    'forget_confirm': forget_confirm
                })
        else:
            try:
                ForgetConfirmView.error_dict.pop(user.phone_number)
            except:
                pass
            forget_confirm.add_error('active_code', 'لطفا ابتدا مجدد به صفحه قبل رفته و دوباره شماره خود را وارد کنید')
            return render(request, 'forget-confirm.html', {
                'errors':True,
                'forget_confirm': forget_confirm
            })


class ChangePasswordView(View):
    def get(self, request, token , code):
        change_form = ChangePasswordForm()
        user = User.objects.filter(token=token , active_mobile=code).first()
        if user is not None:
            return render(request, 'change-password.html', context={
                'change_form': change_form,
                'errors': False
            })

    def post(self, request, token , code):
        change_form = ChangePasswordForm(request.POST)
        user = User.objects.filter(token=token , active_mobile=code).first()
        if user is not None:
            if change_form.is_valid():
                new_password = change_form.cleaned_data.get('new_password')
                re_password = change_form.cleaned_data.get('re_password')
                if len(new_password) > 7:
                    if new_password == re_password:
                        user.set_password(new_password)
                        user.active_mobile = Random_Code.random_code()
                        user.token = get_random_string(70)
                        user.save()
                        return redirect('login_page')
                    else:
                        change_form.add_error('new_password', 'لطفا در وارد کردن تکرار رمز عبور دقت کنید')
                        return render(request, 'change-password.html', context={
                            'change_form': change_form,
                            'errors': True
                        })
                else:
                    change_form.add_error('new_password', 'رمز عبور شما باید شامل حداقل 8 کاراکتر باشد')
                    return render(request, 'change-password.html', context={
                        'change_form': change_form,
                        'errors': True
                    })
            else:
                change_form.add_error('new_password', 'لطفا تمامی فیلدها را بدقت کامل کنید')
                return render(request, 'change-password.html', context={
                    'change_form': change_form,
                    'errors': True
                })
        else:
            user.active_mobile = Random_Code.random_code()
            user.token = get_random_string(70)
            user.save()
            raise Http404


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login_page')

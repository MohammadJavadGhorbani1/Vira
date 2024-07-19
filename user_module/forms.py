from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    firstname = forms.CharField(label='' , widget=forms.TextInput(attrs={'autocomplete':'off' , 'id':'email-user' , 'type':'text' , 'required':'required' , 'placeholder':'نام'}))
    lastname = forms.CharField(label='' , widget=forms.TextInput(attrs={'autocomplete':'off' , 'id':'email-user' , 'type':'text' , 'required':'required' , 'placeholder':'نام خانوادگی'}))
    username = forms.CharField(label='' , widget=forms.TextInput(attrs={'autocomplete':'off' , 'id':'email-user' , 'type':'text' , 'required':'required' , 'placeholder':'نام کاربری'}))
    phone_number = forms.CharField(label='' , widget=forms.TextInput(attrs={'autocomplete':'off' , 'id':'phone-number' , 'type':'text' , 'required':'required' , 'maxlength':'11' , 'placeholder':'شماره تلفن'}))
    password = forms.CharField(label='' , widget=forms.TextInput(attrs={'id':'password-user' , 'type':'password' , 'required':'required' , 'placeholder':'رمز عبور'}))
    re_password = forms.CharField(label='' , widget=forms.TextInput(attrs={'id':'password-user' , 'type':'password' , 'required':'required' , 'placeholder':'تکرار رمز عبور'}))
    # def clean_re_password(self):
    #     password = self.cleaned_data.get('password')
    #     re_password = self.cleaned_data.get('re_password')
    #     if password == re_password:
    #         return re_password
    #     else:
    #         return ValidationError('لطفا در وارد کردن رمز عبور و تکرار آن دقت کنید')

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     if len(password) > 9:
    #         return password
    #     else:
    #         return ValidationError('پسورد شما باید شامل حداقل 8 کاراکتر باشد')

class RegisterConfirmForm(forms.Form):
    active_code = forms.CharField(label='' , widget=forms.TextInput(attrs={'autocomplete':'off' , 'id':'email-user' , 'type':'text' , 'required':'required' , 'placeholder':'کد فعالسازی'}))

class LoginForm(forms.Form):
    # username = forms.CharField(label='' , widget=forms.TextInput(attrs={'id':'email-user' , 'type':'text' , 'required':'required' , 'placeholder':'نام کاربری'}))
    phone_number = forms.CharField(label='' , widget=forms.TextInput(attrs={'autocomplete':'off' , 'id':'phone-number' , 'type':'text' , 'required':'required' , 'maxlength':'11' , 'placeholder':'شماره تلفن'}))
    password = forms.CharField(label='' , widget=forms.TextInput(attrs={'id':'password-user' , 'type':'password' , 'required':'required' , 'placeholder':'رمز عبور'}))

class ForgetPasswordForm(forms.Form):
    phone_number = forms.CharField(label='', widget=forms.TextInput(attrs={'autocomplete': 'off', 'id': 'phone-number', 'type': 'text', 'required': 'required', 'maxlength': '11','placeholder': 'شماره تلفن'}))

class ForgetConfirmForm(forms.Form):
    active_code = forms.CharField(label='' , widget=forms.TextInput(attrs={'autocomplete':'off' , 'id':'email-user' , 'type':'text' , 'required':'required' , 'placeholder':'کد فعالسازی'}))

class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(label='' , widget=forms.TextInput(attrs={'id':'password-user' , 'type':'password' , 'required':'required' , 'placeholder':'رمز عبور جدید'}))
    re_password = forms.CharField(label='' , widget=forms.TextInput(attrs={'id':'password-user' , 'type':'password' , 'required':'required' , 'placeholder':'تکرار رمز عبور جدید'}))

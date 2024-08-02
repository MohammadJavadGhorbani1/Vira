from django import forms
from user_module.models import *

# class EditDashbordForm(forms.Form):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input-first-name' , 'type':'text' , 'name':'billing-first-name' , 'id':'billing-first-name'}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input-last-name' , 'type':'text' , 'name':'billing-last-name' , 'id':'billing-last-name'}))
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'input-display-name' , 'type':'text' , 'name':'billing-display-name' , 'id':'billing-display-name'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-billing-email' , 'type':'text' , 'name':'billing-email' , 'id':'billing-email'}))
#     password = forms.CharField(widget=forms.TextInput(attrs={'class':'input-billing-password' , 'type':'text' , 'name':'billing-password' , 'id':'billing-password'}))
#     re_password = forms.CharField(widget=forms.TextInput(attrs={'class':'input-billing-password' , 'type':'text' , 'name':'billing-password' , 'id':'billing-password'}))
class EditDashbordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_img' , 'first_name' , 'last_name' , 'username' , 'email']
        widgets = {
            'profile_img':forms.FileInput(attrs={'class':'input-profile'}),
            'first_name':forms.TextInput(attrs={'class':'input-first-name' , 'type':'text' , 'name':'billing-first-name' , 'id':'billing-first-name'}),
            'last_name':forms.TextInput(attrs={'class':'input-last-name' , 'type':'text' , 'name':'billing-last-name' , 'id':'billing-last-name'}),
            'username':forms.TextInput(attrs={'class':'input-display-name' , 'type':'text' , 'name':'billing-display-name' , 'id':'billing-display-name'}),
            'email':forms.EmailInput(attrs={'class':'input-billing-email' , 'type':'text' , 'name':'billing-email' , 'id':'billing-email'}),
        }

class EditPasswordDashForm(forms.Form):
    old_password = forms.CharField(widget=forms.TextInput(attrs={'class':'input-billing-password' , 'type':'text' , 'name':'billing-password' , 'id':'billing-password'}))
    new_password = forms.CharField(widget=forms.TextInput(attrs={'class':'input-billing-password' , 'type':'text' , 'name':'billing-password' , 'id':'billing-password'}))
    re_password = forms.CharField(widget=forms.TextInput(attrs={'class':'input-billing-password' , 'type':'text' , 'name':'billing-password' , 'id':'billing-password'}))

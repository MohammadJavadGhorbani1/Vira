from django import forms
import requests

class ContactUsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off' , 'required':'required' , 'class':'input-contact your-name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autocomplete':'off' , 'required':'required' , 'class':'input-contact your-email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off' , 'required':'required' , 'class':'input-contact your-subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'input-contact your-message' , 'cols':'40' , 'rows':'10'}))

class ContactWithEmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autocomplete': 'off', 'required': 'required', 'class': 'input-contact your-email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off', 'required': 'required', 'class': 'input-contact your-subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-contact your-message', 'cols': '40', 'rows': '10'}))

class ContactWithoutEmailForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off', 'required': 'required', 'class': 'input-contact your-subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-contact your-message', 'cols': '40', 'rows': '10'}))

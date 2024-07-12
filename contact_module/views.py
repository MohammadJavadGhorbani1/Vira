from django.http import HttpRequest
from django.shortcuts import render
from .models import *
from .forms import *
from django.views import View

# Create your views here.


class ContactUsView(View):
    def get(self , request):
        contact = ContactUsForm()
        return render(request, 'contact-us_page.html', {
            'contact': contact,
            'error': False,
            'success': False
        })
    def post(self , request):
        contact = ContactUsForm(request.POST)
        if contact.is_valid():
            name = contact.cleaned_data.get('name')
            email = contact.cleaned_data.get('email')
            subject = contact.cleaned_data.get('subject')
            message = contact.cleaned_data.get('message')
            new_message = ContactModel(name=name, email=email, subject=subject, message=message)
            new_message.save()
            return render(request, 'contact-us_page.html', {
                'contact': contact,
                'error': False,
                'success': True
            })
        else:
            return render(request, 'contact-us_page.html', {
                'contact': contact,
                'error': True,
                'success': False
            })

# def contact_us_view(request:HttpRequest):
#     if request.method == 'GET':
#         contact = ContactUsForm()
#         return render(request , 'contact-us_page.html' , {
#         'contact' : contact,
#         'error': False,
#         'success': False
#     })
#     elif request.method == 'POST':
#         contact = ContactUsForm(request.POST)
#         if contact.is_valid():
#             name = contact.cleaned_data.get('name')
#             email = contact.cleaned_data.get('email')
#             subject = contact.cleaned_data.get('subject')
#             message = contact.cleaned_data.get('message')
#             new_message = ContactModel(name=name , email=email , subject=subject , message=message)
#             new_message.save()
#             return render(request, 'contact-us_page.html', {
#                 'contact': contact,
#                 'error': False,
#                 'success': True
#             })
#         else:
#             return render(request, 'contact-us_page.html', {
#                 'contact': contact,
#                 'error': True,
#                 'success': False
#             })
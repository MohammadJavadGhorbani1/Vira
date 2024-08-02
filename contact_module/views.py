from django.http import HttpRequest
from django.shortcuts import render
from .models import *
from .forms import *
from django.views import View
from sitesettings_module.models import *


# Create your views here.


class ContactUsView(View):
    def get(self, request):
        setting = SiteSettingsModel.objects.filter(is_active=True).first()
        contact = ContactUsForm()
        no_email_contact = ContactWithoutEmailForm(request.POST)
        email_contact = ContactWithEmailForm(request.POST)
        return render(request, 'contact-us_page.html', {
            'contact': contact,
            'no_email_contact': no_email_contact,
            'email_contact': email_contact,
            'setting': setting,
            'error': False,
            'success': False
        })

    def post(self, request):
        user = request.user
        setting = SiteSettingsModel.objects.filter(is_active=True).first()
        if user.is_authenticated:
            if user.email:
                no_email_contact = ContactWithoutEmailForm(request.POST)
                if no_email_contact.is_valid():
                    subject = no_email_contact.cleaned_data.get('subject')
                    message = no_email_contact.cleaned_data.get('message')
                    new_message = ContactModel(name=f'{user.first_name} {user.last_name}' , email=user.email , subject=subject , message=message)
                    new_message.save()
                    return render(request, 'contact-us_page.html', context={
                        'no_email_contact':no_email_contact,
                        'error': False,
                        'setting': setting,
                        'success': True
                    })
                else:
                    return render(request, 'contact-us_page.html', context={
                        'no_email_contact': no_email_contact,
                        'error': True,
                        'setting': setting,
                        'success': False
                    })
            else:
                email_contact = ContactWithEmailForm(request.POST)
                if email_contact.is_valid():
                    email = email_contact.cleaned_data.get('email')
                    subject = email_contact.cleaned_data.get('subject')
                    message = email_contact.cleaned_data.get('message')
                    new_message = ContactModel(name=f'{user.first_name} {user.last_name}' , email=email , subject=subject , message=message)
                    new_message.save()
                    return render(request, 'contact-us_page.html', context={
                        'email_contact': email_contact,
                        'error': False,
                        'setting': setting,
                        'success': True
                    })
                else:
                    return render(request, 'contact-us_page.html', context={
                        'email_contact': email_contact,
                        'error': True,
                        'setting': setting,
                        'success': False
                    })
        else:
            contact = ContactUsForm(request.POST)
            if contact.is_valid():
                name = contact.cleaned_data.get('name')
                email = contact.cleaned_data.get('email')
                subject = contact.cleaned_data.get('subject')
                message = contact.cleaned_data.get('message')
                new_message = ContactModel(name=name , email=email , subject=subject , message=message)
                new_message.save()
                return render(request, 'contact-us_page.html', context={
                    'contact': contact,
                    'error': False,
                    'setting': setting,
                    'success': True
                })
            else:
                return render(request, 'contact-us_page.html', context={
                    'contact': contact,
                    'error': True,
                    'setting': setting,
                    'success': False
                })


class AskandAnwserView(View):
    def get(self, request):
        divs = AskandAnwserModel.objects.filter(is_active=True)
        return render(request, 'ask-anwser.html', context={
            'divs': divs,
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

from django.urls import path
from .views import *

urlpatterns = [
    path('contact-us/' , ContactUsView.as_view() , name='contact-us')
]
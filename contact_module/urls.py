from django.urls import path
from .views import *

urlpatterns = [
    path('contact-us/' , ContactUsView.as_view() , name='contact-us'),
    path('ask-anwsers/' , AskandAnwserView.as_view() , name='ask-anwser-page')
]
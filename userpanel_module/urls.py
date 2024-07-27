from django.urls import path
from .views import *

urlpatterns = [
    path('' , MainDashbord.as_view() , name='main-dashbord-page'),
]

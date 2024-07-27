from django.urls import path
from .views import *

urlpatterns = [
    path('register/' , RegisterView.as_view() , name='register_page'),
    path('confirm-code/<token>' , RegisterConfirmView.as_view() , name='confiremcode-page'),
    path('login/' , LoginView.as_view() , name='login_page'),
    path('forget-password/' , ForgetPasswordView.as_view() , name='forget-password-page'),
    path('forget-code/<token>' , ForgetConfirmView.as_view() , name='forget-confirm-page'),
    path('change-password/<token>/<code>' , ChangePasswordView.as_view() , name='change-password-page'),
    path('logout/' , Logout.as_view() , name='logout-page'),
    path('welcome/' , Welcome.as_view() , name='welcome-page'),
]
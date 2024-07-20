from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    profile_img = models.ImageField(upload_to= 'profile_images' , verbose_name='تصویر پروفایل' , null=True)
    phone_number = models.CharField(max_length= 11 , verbose_name= 'شماره تلفن')
    active_mobile = models.CharField(max_length= 6 , verbose_name= 'کد تایید')
    token = models.CharField(max_length=100 , verbose_name='توکن' , null=True)
    def __str__(self):
        return self.phone_number
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

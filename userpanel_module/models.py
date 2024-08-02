from django.db import models
from user_module.models import *
from product_module.models import *

# Create your models here.

class WishlistProducts(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name='کاربر')
    product = models.ForeignKey(Products , on_delete=models.CASCADE , verbose_name='محصول')
    is_active = models.BooleanField(default=True , verbose_name='فعال است/نیست')
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = 'علاقه مندی'
        verbose_name_plural = 'علاقه مندی ها'

class ProductNotifModel(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name='کاربر')
    product = models.ForeignKey(Products , on_delete=models.CASCADE , verbose_name='محصول')
    is_active = models.BooleanField(default=True , verbose_name='فعال است/نیست')
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = 'اطلاع رسانی'
        verbose_name_plural = 'اطلاع رسانی ها'

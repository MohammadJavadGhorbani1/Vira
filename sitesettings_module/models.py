from django.db import models

# Create your models here.

# class SiteSettingsModel(models.Model):
#     logo = models.ImageField(upload_to='logo' , verbose_name='لوگوی سایت')
#     phone = models.CharField(max_length=20 , verbose_name='شماره تماس با ما')
#     email = models.EmailField(verbose_name='ایمیل تماس با ما')
#     about_us = models.TextField(verbose_name='متن درباره ما')
#     def __str__(self):
#         return self.phone
#     class Meta:
#         verbose_name = 'تنظیم'
#         verbose_name_plural = 'تنظیمات'

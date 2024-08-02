from django.db import models

# Create your models here.

class SiteSettingsModel(models.Model):
    logo = models.ImageField(upload_to='logo' , verbose_name='لوگوی سایت')
    phone = models.CharField(max_length=20 , verbose_name='شماره تماس با ما')
    email = models.EmailField(verbose_name='ایمیل تماس با ما')
    location = models.CharField(max_length=200 , verbose_name='مکان')
    about_us = models.TextField(verbose_name='متن درباره ما')
    is_active = models.BooleanField(verbose_name='فعال باشد/نباشد')
    def __str__(self):
        return self.phone
    class Meta:
        verbose_name = 'تنظیم'
        verbose_name_plural = 'تنظیمات'

class SliderSettingsModel(models.Model):
    image = models.ImageField(upload_to='sliders' , verbose_name='تصویر اسلایدر')
    link = models.URLField(max_length=200 , verbose_name='لینک')
    is_active = models.BooleanField(verbose_name='فعال باشد/نباشد')
    def __str__(self):
        return self.link
    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

class AdsSettingsModel(models.Model):
    image = models.ImageField(upload_to='ads' , verbose_name='تصویر')
    link = models.URLField(max_length=200 , verbose_name='لینک')
    is_active = models.BooleanField(verbose_name='فعال باشد/نباشد')
    def __str__(self):
        return self.link
    class Meta:
        verbose_name = 'تبلیغ'
        verbose_name_plural = 'تبلیغات'

class AskandAnwserModel(models.Model):
    question = models.CharField(max_length=300 , verbose_name='سوال')
    anwser = models.TextField(verbose_name='جواب')
    is_active = models.BooleanField(verbose_name='فعال باشد/نباشد' , default=False)
    def __str__(self):
        return self.question
    class Meta:
        verbose_name = 'پرسش و پاسخ'
        verbose_name_plural = 'پرسش و پاسخ ها'

class NotifModel(models.Model):
    title = models.CharField(max_length=200 , verbose_name='عنوان')
    create_date = models.DateTimeField(auto_now_add=True , verbose_name='تاریخ ساخته شدن')
    is_active = models.BooleanField(default=True , verbose_name='فعال باشد/نباشد')
    text = models.TextField(verbose_name='توضیحات')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'اطلاعیه'
        verbose_name_plural = 'اطلاعیه ها'

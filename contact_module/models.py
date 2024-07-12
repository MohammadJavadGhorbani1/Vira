from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=100 , verbose_name='نام')
    email = models.EmailField(max_length=50 , verbose_name='ایمیل')
    subject = models.CharField(max_length=100 , verbose_name='موضوع')
    message = models.TextField(verbose_name='پیغام')
    read_by_admin = models.BooleanField(default=False , verbose_name='خوانده شده/نشده')
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name = 'پیغام'
        verbose_name_plural = 'پیغام ها'

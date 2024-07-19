from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length= 100 , verbose_name='عنوان دسته بندی')
    parent_category = models.ForeignKey('ProductCategory' , on_delete= models.CASCADE , verbose_name='دسته بندی مادر', blank=True, null=True)
    icon = models.CharField(max_length= 100 , verbose_name='آیکون از فونت اوسام', blank=True, null=True)
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name='آدرس دسته بندی در مرورگر')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class ProductTags(models.Model):
    title = models.CharField(max_length= 100 , verbose_name='عنوان تگ')
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name='آدرس تگ در مرورگر')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

class Products(models.Model):
    image = models.ImageField(upload_to='product_imgs' , verbose_name='تصویر محصول' , null=True)
    title = models.CharField(max_length= 100 , verbose_name='عنوان محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    des = models.TextField(max_length= 1000 , null=True , verbose_name='توضیحات')
    off = models.IntegerField(verbose_name='مقدار تخفیف')
    is_active = models.BooleanField(verbose_name='فعال باشد/نباشد')
    category = models.ForeignKey(ProductCategory , on_delete= models.CASCADE , verbose_name='دسته بندی')
    tags = models.ManyToManyField(ProductTags , verbose_name='تگ های مربوطه')
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name='آدرس محصول در مرورگر')
    def __str__(self):
        return self.title
    def Discount(self):
        return int(self.price - (self.off /100) * self.price)
        # gheimat = int(self.price)
        # takhfif = int(self.off)
        # if takhfif > 1:
        #     discount_price = int(gheimat - (gheimat / 100) * takhfif)
        #     self.price_with_off = discount_price
        #     return self.price_with_off
        # else:
        #     return gheimat
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
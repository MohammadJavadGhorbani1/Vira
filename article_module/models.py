from django.db import models

# Create your models here.

class ArticleCategoryModel(models.Model):
    title = models.CharField(max_length=100 , verbose_name='عنوان(خبر/مقاله)')
    is_active = models.BooleanField(default=False , verbose_name='فعال باشد/نباشد')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class ArticleTagModel(models.Model):
    title = models.CharField(max_length=100 , verbose_name='عنوان')
    slug = models.SlugField(unique=True , allow_unicode=True , verbose_name='آدرس در مرورگر')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

class ArticleModel(models.Model):
    image = models.ImageField(upload_to='articles' , verbose_name='تصویر')
    title = models.CharField(max_length=200 , verbose_name='عنوان')
    des = models.TextField(verbose_name='توضیحات')
    create_date = models.DateField(auto_now_add=True , verbose_name='زمان ساخته شدن')
    is_active = models.BooleanField(default=True , verbose_name='فعال باشد/نباشد')
    category = models.ForeignKey(ArticleCategoryModel , on_delete=models.CASCADE , verbose_name='دسته بندی')
    tag = models.ManyToManyField(ArticleTagModel , verbose_name='تگ')
    slug = models.SlugField(unique=True , allow_unicode=True , db_index=True , verbose_name='آدرس در مرورگر')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'وبلاگ'
        verbose_name_plural = 'وبلاگ ها'




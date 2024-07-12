# Generated by Django 4.2.6 on 2024-07-11 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان دسته بندی')),
                ('icon', models.CharField(max_length=100, null=True, verbose_name='آیکون از فونت اوسام')),
                ('slug', models.SlugField(allow_unicode=True, unique=True, verbose_name='آدرس دسته بندی در مرورگر')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.productcategory', verbose_name='دسته بندی مادر')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='ProductTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان تگ')),
                ('slug', models.SlugField(allow_unicode=True, unique=True, verbose_name='آدرس تگ در مرورگر')),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ ها',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان محصول')),
                ('price', models.IntegerField(verbose_name='قیمت محصول')),
                ('des', models.TextField(max_length=1000, null=True, verbose_name='توضیحات')),
                ('off', models.IntegerField(verbose_name='مقدار تخفیف')),
                ('is_active', models.BooleanField(verbose_name='فعال باشد/نباشد')),
                ('slug', models.SlugField(allow_unicode=True, unique=True, verbose_name='آدرس محصول در مرورگر')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.productcategory', verbose_name='دسته بندی')),
                ('tags', models.ManyToManyField(to='product_module.producttags', verbose_name='تگ های مربوطه')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
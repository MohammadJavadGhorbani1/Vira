# Generated by Django 5.0.7 on 2024-07-19 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_products_price_with_off'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='price_with_off',
        ),
    ]
# Generated by Django 5.0.7 on 2024-07-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_remove_products_price_with_off'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='off_time',
            field=models.DateTimeField(null=True, verbose_name='زمان تخفیف'),
        ),
    ]
# Generated by Django 5.0.7 on 2024-07-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال باشد/نباشد'),
        ),
    ]

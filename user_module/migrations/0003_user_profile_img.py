# Generated by Django 5.0.7 on 2024-07-20 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0002_user_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='profile_images', verbose_name='تصویر پروفایل'),
        ),
    ]
